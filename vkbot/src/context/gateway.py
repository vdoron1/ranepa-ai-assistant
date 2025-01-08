import redis.asyncio as redis
from returns.result import Result, Success, Failure

from .interface import ContextInterface
from .types import ContextErrorType, ContextType
from .schemas import Dialog, Message, RoleEnum
from config import CacheConfig


class RedisContextGateway(ContextInterface):
    def __init__(self):
        self._client = redis.Redis(password=CacheConfig.password)

    async def get(self, user_id: int) -> Result[Dialog, ContextErrorType]:
        ...

    async def add(
        self, user_id: int, user_message: str, assistant_message: str
    ) -> Result[ContextType, ContextErrorType]:
        ...

    async def clear(self, user_id: int) -> Result[ContextType, ContextErrorType]:
        ...