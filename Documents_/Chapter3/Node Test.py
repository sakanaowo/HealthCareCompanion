from llama_index.core import Document, SummaryIndex
from llama_index.core.schema import TextNode
from llama_index.core.node_parser import TokenTextSplitter

# Tạo tài liệu
text = "Con mèo ú nằm ườn bên cửa sổ. Tôi muốn mình cũng được như thế."
doc = Document(text=text)

# Chia nhỏ văn bản thành các node
splitter = TokenTextSplitter(chunk_size=20, chunk_overlap=5, separator=" ")
nodes = splitter.get_nodes_from_documents([doc])

# Tạo Index theo 2 cách
index1 = SummaryIndex(nodes)  # Tạo từ Nodes
index2 = SummaryIndex.from_documents([doc])  # Tạo từ Document

# In ra cấu trúc index
print("Index 1:", index1.index_struct)
print("Index 2:", index2.index_struct)
