from vkbottle import API, Bot, BuiltinStateDispenser  # type: ignore

from src import router
from config import AppConfig



from vkbottle import Bot
from src.context.middlewares import RedisMiddleware

bot = Bot("vk1.a.ryCeD1x_Oi-eT4r3A_sncfCzzP3BF4S-cQrHWNRg9NwfldJTF9x_4qBoPO9nAHxBbkRhR7TdKlxXa2Q4imptjdl2uQEGk3sDGgQBOOAfhK2x8ZmQVu_9M8s-CHrkc4Pyd4Z1bLWIFVHoqVz7KrWcoiBEqKunzxXvzLN-tieOAUUJz6etJS6tZJ0ZGpi0EVSWer0KyCtSZUDiCpqMi2OXng")

# Регистрируем Middleware
bot.labeler.message_view.register_middleware(RedisMiddleware)

bot.run_forever()




def run() -> None:
    bot = Bot(AppConfig.bot_config.token)

    bot.labeler.load(router)

    bot.run_forever()


if __name__ == "__main__":
    run()
