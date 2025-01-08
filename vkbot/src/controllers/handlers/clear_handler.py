from returns.result import Success, Failure
from vkbottle.bot import BotLabeler, Message  # type: ignore

from src.useCases import clear_context


clear_router = BotLabeler()


@clear_router.private_message(text="/clear")
async def clear_context_handler(message: Message) -> None:
    """Очищает контекст диалога"""

    match await clear_context(user_id=(await message.get_user()).id):
        case Success(_):
            await message.answer("История диалогов очищена!")
        case Failure(err):
            await message.answer(err.value)
