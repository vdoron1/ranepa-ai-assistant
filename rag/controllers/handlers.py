from fastapi import APIRouter

from service import get_answer
from .schemas import RAGRequest, RAGResponse


router = APIRouter()


@router.post("/get_answer")
async def get_answer(request: RAGRequest) -> RAGResponse:
    return RAGResponse(
        answer=get_answer(
            question=request.query,
            history=request.history
        )
    )
