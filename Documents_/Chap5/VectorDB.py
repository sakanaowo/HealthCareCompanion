# Store vector index using Chroma DB
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex, StorageContext, Document

db = chromadb.PersistentClient(path="database")
chroma_collection = db.get_or_create_collection(name="my_chroma_store")

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

text = "I do love my cat!"
doc = Document(text=text)
index = VectorStoreIndex.from_documents([doc], storage_context=storage_context,)

