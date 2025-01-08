from enum import Enum


class ContextErrorType(str, Enum):
    InvalidParams: str = "Invalid params"
    MemoryError: str = "Memory error"
    InternalError: str = "Internal error"
    KeyError: str = "Key error"


class ContextType(str, Enum):
    Success: str = "Success"
