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
    print(docs[0].text[:1000])
else:
    print("No documents found")

