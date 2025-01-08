from typing import Optional
from returns.result import Result
from abc import ABC, abstractmethod

from .types import AssistantErrorType
from .schemas import AssistantResponse

from src.context import Dialog


class AssistantGatewayInterface(ABC):
    @abstractmethod
    async def answer(
        self, question: str, question_context: Optional[Dialog] = None
    ) -> Result[AssistantResponse, AssistantErrorType]:
        """Возвращает ответ AI-ассистента на вопрос с контекстом диалога"""
        ...
