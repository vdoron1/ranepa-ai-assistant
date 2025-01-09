from typing import List
from langchain.schema import HumanMessage, AIMessage

from controllers.schemas import Message, Role

from .prompt import prompt
from .generate import llm
from .retrieve import retriever


def get_answer(question: str, history: List[Message]) -> str:
    """Stateless-RAG пайплайн"""

    # Приводим историю диалогов из pydantic схем в langchain схемы
    history = [
        HumanMessage(message.content)
        if message.role == Role.User
        else AIMessage(message.content)
        for message in history
    ]

    # Получаем релевантные документы
    docs = retriever.get_relevant_documents(question)

    # Формируем контекст из документов
    context = "\n".join(doc.page_content for doc in docs)

    # Формируем промпт
    query = prompt.invoke({
        "history": history,
        "context": context,
        "question": question
    })

    # Отправляем запрос в модель
    answer = llm(query)

    return answer
