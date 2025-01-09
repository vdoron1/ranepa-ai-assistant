from dataclasses import dataclass
from enum import Enum
from typing import List


class RoleEnum(str, Enum):
    User = "user"
    Assistant = "assistant"


@dataclass
class Message:
    role: RoleEnum
    text: str


@dataclass
class Dialog:
    messages: List[Message]
