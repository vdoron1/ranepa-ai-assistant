import json

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
        result = await self._client.get(name=user_id)

        if result is None:
            return Failure(ContextErrorType.KeyError)

        messages = []
        for item in result:
            # TODO: тут может Failure выкидываться
            message = json.loads(item)
            messages.append(Message(role=RoleEnum(message['role']), text=message['text']))

        return Success(Dialog(messages=messages))

    async def add(
        self, user_id: int, user_message: str, assistant_message: str
    ) -> Result[ContextType, ContextErrorType]:
        await self._client.rpush(
            user_id,
            {"role": RoleEnum.User, "text": user_message},
            {"role": RoleEnum.Assistant, "text": assistant_message},
        )

        return Success(ContextType.Success)

    async def clear(self, user_id: int) -> Result[ContextType, ContextErrorType]:
        await self._client.delete(user_id)
        return Success(ContextType.Success)