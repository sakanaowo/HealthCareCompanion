from typing import Optional

from llama_index.core.agent.react import ReActAgent
from llama_index.core.tools import FunctionTool, QueryEngineTool
from llama_index.core import Document, VectorStoreIndex
from llama_index.agent.openai import OpenAIAgent

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def save_result(result: int) -> None:
    """Save the result to a file."""
    with open("result.txt", "w") as f:
        f.write(str(result))
    return "Result saved to result.txt."


text = "Mèo Ú về dưới cơn mưa tầm tã ngày 4/9/2025"
doc = Document(text=text)
index = VectorStoreIndex.from_documents([doc])

query_engine = index.as_query_engine()

query_tool = QueryEngineTool.from_defaults(
    query_engine=query_engine,
    description="Công cụ tìm kiếm thông tin về mèo ú"
)
multiply_tool = FunctionTool.from_defaults(fn=multiply)
save_result_tool = FunctionTool.from_defaults(fn=save_result)

# openai_agent = OpenAIAgent.from_tools(
#     tools=[query_tool, multiply_tool, save_result_tool],
#     system_prompt="Bạn là RAP NGU, người  bạn tri ký, hiểu chuyện và chân thành",
#     verbose=True
# )

react_agent = ReActAgent.from_tools(
    tools=[query_tool, save_result_tool, multiply_tool],
    system_prompt="Bạn là RAP NGU, người  bạn tri ký, hiểu chuyện và chân thành",
    verbose=True
)
response = react_agent.chat("nhân 5 với 15 giúp tui, và kiểm tra con mèu của tui như thế nào")
print(response)
