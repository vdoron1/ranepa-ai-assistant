from langchain.llms import Ollama

from config import Config

llm = Ollama(model=Config.OLLAMA_MODEL_NAME)
