from retrieval.query_embedder import embed_query
from retrieval.vector_search import search_vectors
from retrieval.context_builder import build_context
from generation.prompt_builder import build_prompt
from generation.llm_generator import generate_answer


def run_rag(question):

    query_embedding = embed_query(question)

    results = search_vectors(query_embedding)

    context = build_context(results)

    prompt = build_prompt(context, question)

    answer = generate_answer(prompt)

    return answer