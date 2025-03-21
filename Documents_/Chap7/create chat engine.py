from llama_index.core import Document, VectorStoreIndex

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

text = "Tôi có một bé mèo, cậu ấy tên là Mèo Ú. Cậu ấy đ ang ngủ bên cửa sổ.Tôi rất quý cậu ấy."
doc = Document(text=text)
index = VectorStoreIndex.from_documents([doc])
chat_engine = index.as_chat_engine()

while True:
    text = input(">>")
    if (text.lower() == "history"):
        print(chat_engine.chat_history)
    else:
        response = chat_engine.stream_chat(text)
        for token in response.response_gen:
            print(token, end="")
