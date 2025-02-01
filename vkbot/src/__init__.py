from vkbottle.bot import BotLabeler
from src.controllers import chat_router, clear_router
from .controllers.middlewares import RegistrationMiddleware


router = BotLabeler()


router.message_view.register_middleware(RegistrationMiddleware)


router.load(clear_router)
router.load(chat_router)

__all__ = ("router",)



