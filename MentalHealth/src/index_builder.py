# tải và tạo mới các index từ các node đầu vào -> lưu trữ trong một folder xác định để sử dụng sau này
from llama_index.core import VectorStoreIndex, load_index_from_storage, StorageContext
from global_settings import INDEX_STORAGE


def build_indexes(nodes):
    try:
        storage_context = StorageContext.from_defaults(
            persist_dir=INDEX_STORAGE
        )
        vector_index = load_index_from_storage(
            storage_context, index_id="vector"
        )
        print("All indices loaded from storage.")
    except Exception as e:
        print(f"Error loading indices from storage: {e}")
        storage_context = StorageContext.from_defaults()
        vector_index = VectorStoreIndex(
            nodes, storage_context=storage_context
        )
        vector_index.set_index_id("vector")
        storage_context.persist(persist_dir=INDEX_STORAGE)
        print("New indices created and persisted.")
    return vector_index
