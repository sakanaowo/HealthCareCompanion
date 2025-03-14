import os

from dotenv import load_dotenv
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

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
