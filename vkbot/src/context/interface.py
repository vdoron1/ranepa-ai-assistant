from abc import ABC, abstractmethod

from returns.result import Result

from .schemas import Dialog, Message
from .types import ContextErrorType, ContextType


class ContextInterface(ABC):
    @abstractmethod
    async def get(self, user_id: int) -> Result[Dialog, ContextErrorType]: ...

    @abstractmethod
    async def add(
        self, user_id: int, user_message: str, assistant_message: str
    ) -> Result[ContextType, ContextErrorType]: ...

    @abstractmethod
    async def clear(self, user_id: int) -> Result[ContextType, ContextErrorType]: ...
