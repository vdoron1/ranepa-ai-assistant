import os
from typing import Optional


from dotenv import load_dotenv
from dataclasses import dataclass

dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

else:
    raise FileNotFoundError("Не нашел файл .env")


@dataclass(frozen=True)
class BotConfig:
    token: Optional[str] = os.getenv("VK_TOKEN")


@dataclass(frozen=True)
class CacheConfig:
    host: Optional[str] = os.getenv("REDIS_HOST")
    port: Optional[str] = os.getenv("REDIS_PORT")
    password: Optional[str] = os.getenv("REDIS_PASSWORD")


@dataclass(frozen=True)
class AppConfig:
    bot_config: BotConfig = BotConfig()
