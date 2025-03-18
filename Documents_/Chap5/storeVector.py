from llama_index.core import StorageContext, load_index_from_storage
from Documents_.Chap5.NodeToIndex import index

index.storage_context.persist(persist_dir="index_cache")

storage_context = StorageContext.from_defaults(
    persist_dir="index_cache"
)
reload_index = load_index_from_storage(storage_context)
