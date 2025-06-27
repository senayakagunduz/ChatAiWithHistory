from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

# Model oluşturuluyor
model = ChatGroq(model_name="llama3-8b-8192", temperature=0.1)

# Oturum geçmişi saklamak için store
store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# Prompt tanımı (düzgün virgüllerle)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer all questions to the best of your ability."),
    MessagesPlaceholder(variable_name="messages")
])

# Zincir oluşturuluyor
chain = prompt | model

# Config içinde session_id belirtiliyor
config = {"configurable": {"session_id": "abcde123"}}

# Geçmiş destekli zincir
with_message_history = RunnableWithMessageHistory(chain, get_session_history)

# Ana giriş noktası
if __name__ == '__main__':
    # true olduğu sürece cevap verecek
    while True:
        user_input = input(">")
        for r in with_message_history.stream(
                input=[
                    HumanMessage(content=user_input)
                ],
                config=config
        ): print(r.content, end=" ")
