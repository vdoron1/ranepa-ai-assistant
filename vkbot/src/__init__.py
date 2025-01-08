from vkbottle.bot import BotLabeler
from .controllers import chat_router, clear_router


router = BotLabeler()

router.load(clear_router)
router.load(chat_router)

__all__ = ("router",)
