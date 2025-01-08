from dataclasses import dataclass


@dataclass
class RagData:
    text: str
    source: str
    confidence: float


@dataclass
class AssistantResponse:
    content_data: RagData
