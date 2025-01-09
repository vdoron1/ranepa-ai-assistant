from enum import Enum


class ContextErrorType(str, Enum):
    InvalidParams = "Invalid params"
    MemoryError = "Memory error"
    InternalError = "Internal error"
    KeyError = "Key error"


class ContextType(str, Enum):
    Success = "Success"
