from vkbottle import API, Bot, BuiltinStateDispenser  # type: ignore

from src import router
from config import AppConfig



def run() -> None:
    bot = Bot(AppConfig.bot_config.token)

    bot.labeler.load(router)

    bot.run_forever()


if __name__ == "__main__":
    run()
