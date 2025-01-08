from enum import Enum


class AssistantErrorType(str, Enum):
    InvalidParams = "Invalid params"
    HighServiceLoad = "High service load"
    InternalError = "Internal error"
