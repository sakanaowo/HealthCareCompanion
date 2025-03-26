import openai
from llama_index.core import Settings, Document, VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.evaluation.batch_runner import BatchEvalRunner
from llama_index.core.evaluation.correctness import CorrectnessEvaluator
from llama_index.core.evaluation.relevancy import RelevancyEvaluator
from llama_index.core.evaluation.faithfulness import FaithfulnessEvaluator
from llama_index.core.llama_dataset.generator import RagDatasetGenerator
import asyncio
import pandas as pd
import nest_asyncio
from tqdm.asyncio import tqdm_asyncio

import os
from dotenv import load_dotenv

load_dotenv()


def setup_openai(api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.2):
    openai.api_key = api_key
    Settings.llm = OpenAI(model=model, temperature=temperature)


def create_document_and_splitter(text: str, chunk_size: int = 20,
                                 chunk_overlap: int = 5, separator: str = " "):
    doc = Document(text=text)
    splitter = TokenTextSplitter(chunk_size=chunk_size,
                                 chunk_overlap=chunk_overlap,
                                 separator=separator)
    nodes = splitter.get_nodes_from_documents([doc])
    return nodes


def create_vector_store_index(nodes):
    vector_index = VectorStoreIndex(nodes)
    query_engine = vector_index.as_query_engine()
    return query_engine


def generate_questions(nodes, num_questions_per_chunk: int = 1):
    dataset_generator = RagDatasetGenerator(nodes, num_questions_per_chunk=num_questions_per_chunk)
    eval_questions = dataset_generator.generate_dataset_from_nodes()
    return eval_questions.to_pandas()


async def evaluate_async(query_engine, df):
    correctness_evaluator = CorrectnessEvaluator()
    faithfulness_evaluator = FaithfulnessEvaluator()
    relevancy_evaluator = RelevancyEvaluator()

    runner = BatchEvalRunner(
        {
            "correctness": correctness_evaluator,
            "faithfulness": faithfulness_evaluator,
            "relevancy": relevancy_evaluator,
        },
        show_progress=True
    )

    eval_result = await runner.aevaluate_queries(
        query_engine=query_engine,
        queries=[question for question in df['query']],
    )
    return eval_result


def aggregate_results(df, eval_result):
    data = []
    for i, quesiton in enumerate(df['query']):
        correctness_result = eval_result['correctness'][i]
        faithfulness_result = eval_result['faithfulness'][i]
        relevancy_result = eval_result['relevancy'][i]
        data.append({
            'Query': quesiton,
            'Correctness Response': correctness_result.response,
            'Corerctness Passing': correctness_result.passing,
            'Correctness Feedback': correctness_result.feedback,
            'Correctness Score': correctness_result.score,
            'Faithfulness Response': faithfulness_result.response,
            'Faithfulness Passing': faithfulness_result.passing,
            'Faithfulness Feedback': faithfulness_result.feedback,
            'Faithfulness Score': faithfulness_result.score,
            'Relevancy Response': relevancy_result.response,
            'Relevancy Passing': relevancy_result.passing,
            'Relevancy Feedback': relevancy_result.feedback,
            'Relevancy Score': relevancy_result.score,
        })
    df_result = pd.DataFrame(data)
    return df_result


def print_average_scores(df):
    correctness_avg = df['Correctness Score'].mean()
    faithfulness_avg = df['Faithfulness Score'].mean()
    relevancy_avg = df['Relevancy Score'].mean()
    print(f"Correctness Average Score: {correctness_avg}")
    print(f"Faithfulness Average Score: {faithfulness_avg}")
    print(f"Relevancy Average Score: {relevancy_avg}")


def main():
    nest_asyncio.apply()

    setup_openai(api_key=os.getenv("OPENAI_API_KEY"))

    text = "Hôm nay trời nắng , tôi đi ăn kem , lạnh buốt cả răng!"
    nodes = create_document_and_splitter(text)

    query_engine = create_vector_store_index(nodes)

    df = generate_questions(nodes)

    eval_result = asyncio.run(evaluate_async(query_engine, df))
    df_result = aggregate_results(df, eval_result)
    print_average_scores(df_result)


if __name__ == "__main__":
    main()
