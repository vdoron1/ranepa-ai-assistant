from pydantic import BaseModel
from typing import List
from enum import Enum


class Role(Enum):
    User = "user"
    Assistant = "assistant"


class Message(BaseModel):
    role: Role
    content: str


class RAGRequest(BaseModel):
    prompt: str
    history: List[Message]


class RAGResponse(BaseModel):
    answer: str
