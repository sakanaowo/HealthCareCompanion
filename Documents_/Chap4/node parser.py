from llama_index.core.node_parser import SimpleNodeParser
from llama_index.readers.file import FlatReader
from pathlib import Path

md_docs = FlatReader().load_data(Path("files/md_test.md"))

parser = SimpleNodeParser()
md_nodes = parser.get_nodes_from_documents(md_docs)
print(md_nodes[0])
