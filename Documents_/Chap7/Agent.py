import datetime

from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools import FunctionTool, QueryEngineTool
from llama_index.core import Document, VectorStoreIndex

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def get_time():
    """Get current date and time.
    Returns:
        str:Current date and time.
    """
    now = datetime.datetime.now()
    return now.strftime("%Y-%m%d %H:%M:%S")


get_date_time_tool = FunctionTool.from_defaults(get_time)

text = "Mèo Ú bị sập bẫy do đi về muộn"
doc = Document(text=text)
index = VectorStoreIndex.from_documents([doc])

query_engine = index.as_query_engine()
query_tool = QueryEngineTool.from_defaults(query_engine=query_engine,
                                           description="Công cụ tìm kiếm thông tin về mèo Ú")
agent = OpenAIAgent.from_tools(tools=[query_tool, get_date_time_tool])

response1 = agent.chat("Mấy giờ rùi?")
response2 = agent.chat("Mèo ú của tôi đang ở đâu")

print(response1)
print(response2)
