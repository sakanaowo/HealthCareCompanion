import os
import json
from datetime import datetime
from llama_index.core import load_index_from_storage, StorageContext
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.tools import QueryEngineTool, ToolMetadata, FunctionTool
from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.agent.openai import OpenAIAgent
from global_settings import INDEX_STORAGE, CONVERSATION_FILE, SCORES_FILE
from .prompts import CUSTORM_AGENT_SYSTEM_TEMPLATE


def load_chat_store():
    if os.path.exists(CONVERSATION_FILE) and os.path.getsize(CONVERSATION_FILE) > 0:
        try:
            chat_store = SimpleChatStore.from_persist_path(CONVERSATION_FILE)
        except json.JSONDecodeError:
            chat_store = SimpleChatStore()
    else:
        chat_store = SimpleChatStore()
    return chat_store


def save_score(score, content, total_guess, username):
    """write score and content to file
    Args:
        score (string): Score of the user's mental health.
        content (string): Content of the user's mental health.
        total_guess (string): Total guess of the user's mental health.
    """

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = {
        "username": username,
        "Time": current_time,
        "Score": score,
        "Content": content,
        "Total_Guess": total_guess
    }

    # read data if data file exist
    try:
        with open(SCORES_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # append new data
    data.append(new_entry)

    # write back
    with open(SCORES_FILE, "w") as file:
        json.dump(data, file, indent=4)


def display_messages(chat_store, container, key):
    messages = chat_store.get_messages(key)
    if not messages:
        print("No messages found.")
        return
    for msg in messages:
        print(msg.content)


def initialize_chatbot(chat_store, container, username, user_info):
    memory = ChatMemoryBuffer.from_defaults(
        token_limit=3000,
        chat_store=chat_store,
        chat_store_key=username
    )
    storage_context = StorageContext.from_defaults(
        persist_dir=INDEX_STORAGE
    )
    index = load_index_from_storage(
        storage_context, index_id="vector"
    )
    dsm5_engine = index.as_query_engine(
        similarity_top_k=3,
    )
    dsm5_tool = QueryEngineTool(
        query_engine=dsm5_engine,
        metadata=ToolMetadata(
            name="dsm5",
            description=(
                f"Cung cấp thông tin liên quan đến các bệnh"
                f"tâm thần theo tiêu chuẩn DSM-5. Sử dụng câu hỏi văn bản thuần túy chi tiết làm đầu vào cho công cụ"
            ),
        )
    )
    save_tool = FunctionTool.from_defaults(fn=save_score)
    agent = OpenAIAgent.from_tools(
        tools=[dsm5_tool, save_tool],
        memory=memory,
        system_prompt=CUSTORM_AGENT_SYSTEM_TEMPLATE.format(userinfo=user_info)
    )
    display_messages(chat_store, container, key=username)
    return agent
