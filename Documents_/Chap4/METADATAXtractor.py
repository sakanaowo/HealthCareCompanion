import os

from dotenv import load_dotenv
from llama_index.core.extractors import TitleExtractor, KeywordExtractor
from llama_index.core.node_parser import SemanticSplitterNodeParser
import nltk
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import SimpleDirectoryReader
import nest_asyncio
from llama_index.core.extractors import QuestionsAnsweredExtractor
from llama_index.extractors.entity import EntityExtractor
from llama_index.core.extractors import SummaryExtractor

# nltk.download('all')
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
nest_asyncio.apply()

reader = SimpleDirectoryReader(
    input_files=["files/md_test.md"]
)
docs = reader.load_data()
embed_model = OpenAIEmbedding()
splitter = SemanticSplitterNodeParser(
    buffer_size=1,
    breakpoint_percentile_threshold=95,
    embed_model=embed_model
)
nodes = splitter.get_nodes_from_documents(docs)
### Title xtractor
# title_extractor = TitleExtractor()
# metadata_list = title_extractor.extract(nodes)
# for i in metadata_list:
#     print(i)

### Question Extractor
DEFAULT_TITLE_NODE_TEMPLATE = """\
Context : { context_str }. Give a title that summarizes all of \
the unique entities , titles or themes found in the context . Title : """
CUSTORM_QUESTION_GEN_TMPL = """\
Here is the context :
{ context_str }

Given the contextual information , \
generate { num_questions } questions this context can provide \
specific answers to which are unlikely to be found elsewhere .

Higher - level summaries of surrounding context may be provided \
as well . Try using these summaries to generate better questions \
that this context can answer .

L ư u ý : H ã y tr ả v ề k ết qu ả b ằ ng ti ế ng Vi ệ t .
"""
### qa_extractor = QuestionsAnsweredExtractor(questions=3, prompt_template=CUSTORM_QUESTION_GEN_TMPL)
# metadata_list = qa_extractor.extract(nodes)
# for i in metadata_list:
#     print(i)

### summary extractor
custom_summary_extract_template = """
Here is the content of the section :
{ context_str }

Summarize the key topics and entities of the section . \
Lưu ý: Hãy trả về kết quả bằng tiếng Việt.\
Summary : """
# summary_extractor = SummaryExtractor(
#     summaries=["prev", "self", "next"],
#     prompt_template=custom_summary_extract_template
# )
# metadata_list = summary_extractor.extract(nodes)
# print(metadata_list)
### keywordExtractor
# key_extractor = KeywordExtractor( keywords =3)
# metadata_list = key_extractor.extract ( nodes )
# print ( metadata_list )

entity_extractor = EntityExtractor(
    device="cpu"
)
metadata_list = entity_extractor.extract(nodes)
print(metadata_list)
