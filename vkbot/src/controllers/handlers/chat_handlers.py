from returns.result import Success, Failure
from vkbottle.bot import BotLabeler, Message  # type: ignore

from src.useCases import get_answer
from src.controllers.keyboards import DidAnsweredKeyboard


chat_router = BotLabeler()


@chat_router.private_message()
async def question_handler(message: Message) -> None:
    user = await message.get_user()

    match await get_answer(user_id=user.id, question=message.text):
        case Failure(err):
            return await message.answer(err.value)

        case Success(response):
            await message.answer(
                response.content_data.text + "\n\nЯ ответил на ваш вопрос?",
                keyboard=DidAnsweredKeyboard.get_json(),
            )
