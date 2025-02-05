import json
import redis.asyncio as redis
import subprocess
from returns.result import Success, Failure
from vkbottle.bot import BotLabeler, Message  # type: ignore
from src.controllers.keyboards import DidAnsweredKeyboard
import sys


chat_router = BotLabeler()
redis_client = redis.Redis.from_url("redis://127.0.0.1:6379", encoding="utf-8", decode_responses=True)

class ContextErrorType:
    KeyError = "ContextErrorType.KeyError"
    UnknownError = "ContextErrorType.UnknownError"

async def llama_generate(prompt: str):
    """Генерирует ответ с использованием Ollama"""
    try:
        # Преобразуем строку в UTF-8 перед передачей в Ollama
        result = subprocess.run(
            ['ollama', 'run', 'llama3.2', prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Убедимся, что вывод в текстовой кодировке
            encoding="utf-8"  # Устанавливаем правильную кодировку для вывода
        )
        
        response_text = result.stdout.strip()
        if result.stderr:
            print(f"❌ Ошибка Ollama: {result.stderr}")
        
        return response_text

    except Exception as e:
        print(f"❌ Ошибка при вызове Ollama: {e}")
        return "Произошла ошибка при генерации ответа."

async def get_user_context(user_id: int, new_message=None):
    """Получаем и обновляем историю сообщений пользователя"""
    user_context = await redis_client.get(f"user_context:{user_id}")
    user_context = json.loads(user_context) if user_context else {"user_id": user_id, "history": []}

    if new_message:
        user_context["history"].append(new_message)
        if len(user_context["history"]) > 10:  # Храним последние 10 сообщений
            user_context["history"].pop(0)

    await redis_client.set(f"user_context:{user_id}", json.dumps(user_context))
    return user_context

async def get_answer(user_id: int, question: str):
    """Генерирует ответ с использованием модели LLaMA через Ollama"""
    user_context = await get_user_context(user_id, new_message=question)

    if not user_context or "history" not in user_context:
        return Failure("Ошибка: контекст пользователя не найден.")

    # Формируем запрос с учетом истории
    prompt = "\n".join(user_context["history"]) + f"\nПользователь: {question}\nLLaMA:"

    # Генерация ответа через Ollama
    response_text = await llama_generate(prompt)

    # Проверяем, не является ли ответ повтором
    if response_text in user_context["history"]:
        return Failure("Ответ повторяется, прекращаем обработку.")

    # Сохраняем ответ в историю
    user_context["history"].append(f"LLaMA: {response_text}")
    await redis_client.set(f"user_context:{user_id}", json.dumps(user_context))

    return Success({"content_data": {"text": response_text}})

@chat_router.private_message()
async def question_handler(message: Message) -> None:
    """Обрабатывает входящие сообщения и отправляет ответ через LLaMA"""
    user = await message.get_user()

    result = await get_answer(user.id, message.text)
    if isinstance(result, Failure):
        return await message.answer(f"Ошибка: {result.failure()}")
    
    response_data = result.unwrap()
    if "content_data" in response_data and "text" in response_data["content_data"]:
        await message.answer(
            response_data["content_data"]["text"] + "\n\nЯ ответил на ваш вопрос?",
            keyboard=DidAnsweredKeyboard.get_json(),
        )

@chat_router.private_message(text="/clear")
async def clear_context_handler(message: Message) -> None:
    """Очищает историю сообщений пользователя"""
    user = await message.get_user()
    user_key = f"user_context:{user.id}"

    if await redis_client.exists(user_key):
        await redis_client.delete(user_key)
        await message.answer("✅ История диалога очищена.")
    else:
        await message.answer("ℹ️ Контекст уже пуст.")
