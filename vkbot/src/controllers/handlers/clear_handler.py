import redis.asyncio as redis
from returns.result import Success, Failure
from vkbottle.bot import BotLabeler, Message  # type: ignore
from src.useCases import clear_context

clear_router = BotLabeler()
redis_client = redis.Redis.from_url("redis://127.0.0.1:6379", encoding="utf-8", decode_responses=True)

@clear_router.private_message(text="/clear")
async def clear_context_handler(message: Message) -> None:
    """Очищает контекст диалога"""

    user = await message.get_user()
    user_key = f"user:{user.id}"

    # Проверяем, есть ли пользователь в Redis, и очищаем его контекст
    if await redis_client.exists(user_key):
        await redis_client.delete(user_key)  # Удаляем контекст пользователя
        await message.answer("✅ Контекст диалога очищен.")
    else:
        await message.answer("ℹ️ Контекст уже пуст.")

    # Вызываем функцию clear_context для дополнительной очистки
    match await clear_context(user_id=user.id):
        case Success(_):
            await message.answer("✅ История диалога полностью очищена!")
        case Failure(err):
            await message.answer(f"❌ Ошибка: {err.value}")
