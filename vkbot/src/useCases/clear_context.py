from returns.result import Result

from src.context import RedisContextGateway, ContextErrorType, ContextType

context = RedisContextGateway()


async def clear_context(user_id: int) -> Result[ContextType, ContextErrorType]:
    return await context.clear(user_id=user_id)
