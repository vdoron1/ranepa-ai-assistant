from typing import Optional

from returns.result import Result, Success, Failure

from .types import AssistantErrorType  # type: ignore
from .interface import AssistantGatewayInterface  # type: ignore
from .schemas import AssistantResponse,  RagData  # type: ignore

from src.context import Dialog


class MockAssistantGateway(AssistantGatewayInterface):

    async def answer(
        self, question: str, question_context: Optional[Dialog] = None
    ) -> Result[AssistantResponse, AssistantErrorType]:

        return Success(
            AssistantResponse(
                content_data=AssistantResponse(
                    elements=[
                        "Первый вариант вопроса",
                        "Второй вариант вопроса",
                        "Третий вариант вопроса",
                    ],
                    source="Сам придумал",
                ),
            )
        )
