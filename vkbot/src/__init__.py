from vkbottle.bot import BotLabeler
from .controllers import chat_router, clear_router
from .controllers.middlewares import NoBotMiddleware, RegistrationMiddleware, InfoMiddleware


router = BotLabeler()


router.message_view.register_middleware(NoBotMiddleware())
router.message_view.register_middleware(RegistrationMiddleware())
router.message_view.register_middleware(InfoMiddleware())


router.load(clear_router)
router.load(chat_router)

__all__ = ("router",)



