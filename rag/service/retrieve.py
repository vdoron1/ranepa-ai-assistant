from qdrant_client import QdrantClient
from qdrant_client.grpc import VectorParams
from langchain.vectorstores import Qdrant as LangchainQdrant

from config import Config
from vectorize import embed

storage_client = QdrantClient(host=Config.QDRANT_HOST, port=Config.QDRANT_PORT)


def create_if_not_exists():
    """Миграции схем данных"""

    collection_names = [col.name for col in storage_client.get_collections().collections]

    if Config.COLLECTION_NAME not in collection_names:
        storage_client.create_collection(
            collection_name=Config.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=Config.VECTOR_SIZE,
                distance=Config.DISTANCE_METRIC
            )
        )


vector_store = LangchainQdrant(
    client=storage_client,
    collection_name=Config.COLLECTION_NAME,
    embedding_function=embed
)

# не, LangChain конечно молодцы, что у них фреймворк тянется с сервисов до адаптеров
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)


def add_document(document) -> None:
    ...