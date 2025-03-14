import os

from dotenv import load_dotenv
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
text = """ Hôm nay Sài Gòn mưa quá, thèm một chiếc kem lạnh thấu tâm can .
Ngoài trời mưa vẫn rơi như trút, tôi thì cạn khô!
"""

doc = Document(text=text)
# create pipeline
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=50, chunk_overlap=0),
        TitleExtractor(),
        OpenAIEmbedding(),
    ]
)

# run pipeline
nodes = pipeline.run(documents=[doc])
for node in nodes:
    print(node)
    print(node.metadata)
pipeline.persist("pipeline_cache")

new_pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=50, chunk_overlap=0),
        TitleExtractor(),
        OpenAIEmbedding(),
    ]
)
new_pipeline.load("pipeline_cache")
nodes = new_pipeline.run(documents=[doc])
for node in nodes:
    print(node)
