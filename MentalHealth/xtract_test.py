import openai
from llama_index.core import Document, Settings
from llama_index.core.extractors import SummaryExtractor, TitleExtractor
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SemanticSplitterNodeParser
import streamlit as st
import openai
from llama_index.llms.openai import OpenAI


def setup_openai(api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.2):
    openai.api_key = api_key
    Settings.llm = OpenAI(model=model, temperature=temperature)


api_key = st.secrets.openai.OPENAI_API_KEY
setup_openai(api_key)

text = """ Mèo rất đáng yêu.
Acid hydrochloric đậm đặc nhất có nồng độ tối đa là 40%.
Ở dạng đậm đặc, acid này có thể tạo thành các sương mù acid ,
chúng đều có khả năng ăn mòn các mô con người, gây tổn thương cơ quan hô hấp,
mắt, da và ruột. """

CUSTORM_QUESTION_GEN_TMPL = """\
Here is the context :
{context_str}

Given the contextual information , \
generate {num_questions} questions this context can provide \
specific answers to which are unlikely to be found elsewhere .

Higher - level summaries of surrounding context may be provided \
as well . Try using these summaries to generate better questions \
that this context can answer .

Lưu ý : Hãy trả về kết quả bằng tiếng iệt.
"""

print(CUSTORM_QUESTION_GEN_TMPL.format(context_str=text, num_questions=3))

#
# doc = Document(text=text)
#
# embed_model = OpenAIEmbedding()
# splitter = SemanticSplitterNodeParser(
#     buffer_size=1,
#     breakpoint_percentile_threshold=95,
#     embed_model=embed_model
# )
# nodes = splitter.get_nodes_from_documents([doc])
# # for node in nodes:
# #     print(node)
# # title_extractor = TitleExtractor()
# # metadata_list = title_extractor.extract(nodes)
# # for metadata in metadata_list:
# #     print(metadata)
# summary_extractor = SummaryExtractor(
#     summaries=["prev", "self", "next"],
#     prompt_template=CUSTORM_QUESTION_GEN_TMPL.format(context_str=text, num_questions=3)
# )
# metadata_list = summary_extractor.extract(nodes)
# for metadata in metadata_list:
#     print(metadata)
