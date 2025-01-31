from vkbottle.dispatch.middlewares import BaseMiddleware
import redis.asyncio as redis
from config import CacheConfig

class RedisMiddleware(BaseMiddleware):
    def __init__(self):
        self._client = redis.Redis(password=CacheConfig.password)

    async def pre(self):
        user_id = self.event.object.message.from_id  # Получаем user_id
        user_exists = await self._client.exists(user_id)
        
        if not user_exists:
            await self._client.set(user_id, "new_user")  # Добавляем нового пользователя
        
        return self.event
