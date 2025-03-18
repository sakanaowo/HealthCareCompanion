import os

from dotenv import load_dotenv
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor, QuestionsAnsweredExtractor
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core import VectorStoreIndex

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

text = """ Mèo rất đáng yêu.
Acid hydrochloric đậm đặc nhất có nồng độ tối đa là 40%.
Ở dạng đậm đặc, acid này có thể tạo thành các sương mù acid ,
chúng đều có khả năng ăn mòn các mô con người, gây tổn thương cơ quan hô hấp,
mắt, da và ruột.
"""
doc = Document(text=text)

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=50, chunk_overlap=0),
        TitleExtractor(),
        OpenAIEmbedding(),
    ]
)

nodes = pipeline.run(documents=[doc])

index = VectorStoreIndex(nodes)
