import openai
from llama_index.core import Document, Settings
from llama_index.core.extractors import SummaryExtractor
from llama_index.legacy import OpenAIEmbedding
from llama_index.legacy.node_parser import SemanticSplitterNodeParser
import streamlit as st
import openai
from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def setup_openai(api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.2):
    openai.api_key = api_key
    Settings.llm = OpenAI(model=model, temperature=temperature)


api_key = st.secrets.openai.OPENAI_API_KEY
setup_openai(api_key)

text = """ Mèo rất đáng yêu.
Acid hydrochloric đậm đặc nhất có nồng độ tối đa là 40%.
Ở dạng đậm đặc, acid này có thể tạo thành các sương mù acid ,
chúng đều có khả năng ăn mòn các mô con người, gây tổn thương cơ quan hô hấp,
mắt, da và ruột. """

doc = Document(text=text)

embed_model = OpenAIEmbedding()
splitter = SemanticSplitterNodeParser(
    buffer_size=1,
    breakpoint_percentile_threshold=95,
    embed_model=embed_model
)
nodes = splitter.get_nodes_from_documents([doc])
for node in nodes:
    print(node)
