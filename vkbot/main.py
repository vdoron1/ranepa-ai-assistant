from vkbottle import API, Bot, BuiltinStateDispenser  # type: ignore

from src import router
from config import AppConfig



from vkbottle import Bot
from src.context.middlewares import RedisMiddleware




def run() -> None:
    bot = Bot(AppConfig.bot_config.token)
    bot.labeler.message_view.register_middleware(RedisMiddleware)

    bot.labeler.load(router)

    bot.run_forever()


if __name__ == "__main__":
    run()
