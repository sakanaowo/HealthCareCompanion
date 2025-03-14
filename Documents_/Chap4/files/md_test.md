# Loading data

### SimpleDirecoryReader

- Được dùng để đọc tài liệu:
    - PDF
    - Word
    - CSV
    - TXT
- Mục tiêu: tạo thư mục chứa các loại dữ liệu và đưa cho `SimpleDirectoryReader`
- Cú pháp:

    ```python
    from llama_index.core import SimpleDirectoryReader
    
    document = SimpleDirectoryReader(input_dir=str, input_files=List, recursive=bool)
    ```

    - Explain:
        - `input_dir` : đường dẫn đến thư mục chứa data muốn nạp
        - `input_files` : Danh sách các tệp cụ thể, mặc định `None`
        - `recursive` :
            - Nếu đặt True → nó tìm kiếm và nạp dữ liệu từ tất cả các thư mục con bên trong `input_dir`
            - Ngược lại → chỉ nạp các tệp trong thư mục chính

    ```python
    from llama_index.core import SimpleDirectoryReader 
    STORAGE_PATH = "docx"
    documents = SimpleDirectoryReader(
    	STORAGE_PATH,
    	recursive=True
    )
    for i in documents[0]:
    	print(i)
    ```


### SimpleWebPageReader

- Công cụ tải nội dung từ các web trực tiếp vào LlamaIndex
- Chuyển đổi HTML → văn bản
- Cú pháp:

    ```python
    reader = SimpleWebPageReader(html_to_text=True)
    pages = reader.load_data(urls=["URL...",...]
    ```


### LlamaParse

- Nền tảng phân tích tài liệu
- Mục đích chính là phân tích và làm sạch dữ liệu
- Chức năng chính:
    - Trích xuất văn bản hiện đại

Ví dụ:

```python
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LLAMA_CLOUD_API_KEY"] = os.getenv("LLAMA_CLOUD_API_KEY")
parser = LlamaParse(result_type="text")
file_extractor = {".pdf": parser}
reader = SimpleDirectoryReader(
    "/Documents_/Chap4/files",
    file_extractor=file_extractor,
)
docs = reader.load_data()
if docs:
    print(docs[0].text[:1000])  # in ra 1000 
else:
    print("No documents found")
```

note:

- Phải tạo file `.env` lưu key API trước

# Kỹ thuật tạo Node

## SimpleNodeParser

## Bộ chia văn bản - Splitter

# Khai thác Metadata (Metadata Extraction)

# Ingestion Pipeline