from returns.result import Result, Failure, Success
from returns.pipeline import is_successful

from src.context import Dialog, RedisContextGateway, ContextErrorType
from src.assistant import (
    MockAssistantGateway,
    AssistantResponse,
    AssistantErrorType,
)

assistant = MockAssistantGateway()
context = RedisContextGateway()


# TODO: заменить на монадические вычисления
async def get_answer(
    user_id: int, question: str
) -> Result[AssistantResponse, AssistantErrorType | ContextErrorType]:
    """Отвечает на вопрос пользователя и обновляет контекст диалога"""

    question_context: Result[Dialog, ContextErrorType] = await context.get(
        user_id=user_id
    )

    if not is_successful(question_context):
        return Failure(question_context.failure())

    answer = await assistant.answer(
        question=question, question_context=question_context.unwrap()
    )

    if not is_successful(answer):
        return answer

    response: AssistantResponse = answer.unwrap()

    await context.add(
        user_id=user_id,
        user_message=question,
        assistant_message=response.content_data.text,  # type: ignore
    )

    return answer
