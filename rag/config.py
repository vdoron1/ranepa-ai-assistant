import os
from dataclasses import dataclass
from qdrant_client.models import Distance


@dataclass
class Config:
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", "6333"))
    COLLECTION_NAME: str = "documents"
    VECTOR_SIZE: int = 768  # Размер вектора для RuBERT
    DISTANCE_METRIC: str = Distance.COSINE
    OLLAMA_MODEL_NAME: str = "llama-3.1-8b"
