from llama_index.readers.web import SimpleWebPageReader

reader = SimpleWebPageReader()
pages = reader.load_data(urls=["https://minhbeo.netlify.app/"])
print(pages[0].text)
