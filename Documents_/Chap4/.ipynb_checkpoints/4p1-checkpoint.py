from llama_index.core import SimpleDirectoryReader

# Đọc file trong Chap4
documents = SimpleDirectoryReader(input_dir="Chap4", input_files=["tmp.docx"], recursive=False).load_data()

# In nội dung file
for doc in documents:
    print(doc.text)  # Lấy nội dung file
