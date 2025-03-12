from llama_index.core import Document

text = "AI VIET NAM"
doc = Document(
    text=text,
    metadata={
        "fb": "fb/ aivietnam .edu.vn"
    },
    id_="1"
)
for i in doc:
    print(i)
