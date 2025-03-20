from llama_index.core import Document, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import SummaryIndex, SimpleDirectoryReader, get_response_synthesizer

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

"""Khoi tao document va index"""

text = """ Mèo rất đáng yêu.
Acid hydrochloric đậm đặc nhất có nồng độ tối đa là 40%.
Ở dạng đậm đặc, acid này có thể tạo thành các sương mù acid ,
chúng đều có khả năng ăn mòn các mô con người, gây tổn thương cơ quan hô hấp,
mắt, da và ruột."""

doc = Document(text=text)

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=50, chunk_overlap=0),
        TitleExtractor(),  # trich xuat tieu de tu tai lieu
        OpenAIEmbedding(),
    ]
)
# run pipeline
nodes = pipeline.run(documents=[doc])
# nodes to index
index = VectorStoreIndex(nodes)

"""thiet lap thanh phan he thong"""
# tao cong cu truy xuat
retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=2  # chi lay 2 kq tuong dong cao nhat
)

# tong hop phan hoi
response_synthesizer = get_response_synthesizer(
    response_mode="tree_summarize",
    verbose=True  # tham so hien thi chi tiet qua trinh truy van -> theo doi cach tao ra phan hoi
)

# bo xu ly hau ki
pp = SimilarityPostprocessor(similarity_cutoff=0.5)
# ngưỡng tương đồng tối thiểu là 0,5

# tong hop
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
    node_postprocessors=[pp]
)

if __name__ == "__main__":
    response = query_engine.query(
        "mèo rất đáng yêu đúng hong ?"
    )
    print(response)
