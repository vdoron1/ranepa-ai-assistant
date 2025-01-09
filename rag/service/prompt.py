from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

system = """
Ты полезный цифровой ассистент высшего учебного заведения РАНХиГС
Используйте приведенные ниже фрагменты из извлеченного контекста и историю диалога, чтобы ответить на вопрос.
Если вы не знаете ответа, просто скажите, что вы не знаете. 
Используйте максимум три предложения и старайся, чтобы ответ был кратким.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "History: {history}"),
    ("human", "Context: {context}"),
    ("human", "Question: {question}")
])
