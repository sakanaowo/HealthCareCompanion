import os

from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.extractors import SummaryExtractor
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_parse import LlamaParse
import openai
import streamlit as st
from dotenv import load_dotenv

from .prompts import CUSTORM_QUESTION_GEN_TMPL
from .global_settings import STORAGE_PATH, FILES_PATH, CACHE_FILE

load_dotenv()

os.environ["LLAMA_CLOUD_API_KEY"] = os.getenv("LLAMA_CLOUD_API_KEY")

openai.api_key = st.secrets.openai.OPENAI_API_KEY
Settings.llm = OpenAI(model='gpt-4o-mini', temperature=0.2)  # độ ngẫu nhiên = 0,2


# CUSTORM_QUESTION_GEN_TMPL = """\
# Here is the context :
# {context_str}
#
# Given the contextual information , \
# generate {num_questions} questions this context can provide \
# specific answers to which are unlikely to be found elsewhere .
#
# Higher - level summaries of surrounding context may be provided \
# as well . Try using these summaries to generate better questions \
# that this context can answer .
#
# Lưu ý : Hãy trả về kết quả bằng tiếng iệt.
# """

# đọc dữ liệu thô bằng Simple Directory Reader
# id là đường dẫn tuyệt đối -> không thể share
def ingest_document():
    """Load documents, but cant move or share"""
    parser = LlamaParse(result_type="text")
    file_extractor = {".pdf": parser}
    documents = SimpleDirectoryReader(
        input_files=FILES_PATH,
        file_extractor=file_extractor,
        filename_as_id=True
    ).load_data()
    for doc in documents:
        print(doc)

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
