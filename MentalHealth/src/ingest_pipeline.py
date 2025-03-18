from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.extractors import SummaryExtractor
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
import openai
import streamlit as st

from Documents_.Chap4.METADATAXtractor import CUSTORM_QUESTION_GEN_TMPL
from global_settings import STORAGE_PATH, FILES_PATH, CACHE_FILE

openai.api_key = st.secrets.openai_key.OPENAI_API_KEY
Settings.llm = OpenAI(model='gpt-4o-mini', temperature=0.2)  # độ ngẫu nhiên = 0,2

# đọc dữ liệu thô bằng Simple Directory Reader
# id là đường dẫn tuyệt đối -> không thể share
def ingest_document():
    """Load documents, but cant move or share"""
    documents = SimpleDirectoryReader(
        input_files=FILES_PATH,
        filename_as_id=True
    ).load_data()
    for doc in documents:
        print(doc.text)

    # kiểm tra nếu đã có cache, không có -> tạo mới
    try:
        cached_hashes = IngestionCache.from_persist_path(CACHE_FILE)
        print(cached_hashes)
    except:
        cached_hashes = ""
        print("No cache found. Running without cache...")
    # Tạo tóm tắt tại chính node hiện tại -> 'self'
    pipeline = IngestionPipeline(
        transformations=[
            TokenTextSplitter(chunk_size=512,
                              chunk_overlap=20),
            SummaryExtractor(summaries=['self'],
                             prompt_template=CUSTORM_QUESTION_GEN_TMPL),
            OpenAIEmbedding()
        ],
        cache=cached_hashes
    )
    # tạo node bằng pipeline vừa tạo và lưu lại bộ đệm trong CACHE_FILE 
    nodes = pipeline.run(documents=documents)
    pipeline.cache.persist(CACHE_FILE)

    return nodes
