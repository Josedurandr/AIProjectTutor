from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from database import CTGrammar, CTUser, CTText, CTVocabulary
from langchain.chat_models import ChatOpenAI
import openai
from dotenv import load_dotenv
load_dotenv(override=False)

chat = ChatOpenAI()
chat([HumanMessage(content="Translate this sentence from English to French: I love programming.")])
AIMessage(content="J'adore la programmation.", additional_kwargs={}, example=False)