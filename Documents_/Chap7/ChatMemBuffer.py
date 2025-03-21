from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core import Document, VectorStoreIndex
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
text = "Mèo Ú đi lạc, mấy ngày rồi cậu ấy không về nhà, tôi lo quá!"

doc = Document(text=text)

index = VectorStoreIndex.from_documents([doc])

try:
    chat_store = SimpleChatStore.from_persist_path(
        persist_path="chat_memory.json"
    )
except FileNotFoundError:
    chat_store = SimpleChatStore()

memory = ChatMemoryBuffer.from_defaults(
    token_limit=20,
    chat_store=chat_store,
    chat_store_key="User 1"
)

chat_engine = index.as_chat_engine(memory=memory)
while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        break
    response = chat_engine.chat(user_input)
    print("Bot:", response)

print(chat_engine.chat_history)
chat_store.persist(persist_path="chat_memory.json")
