from pipelines.rag_pipeline import run_rag


def restaurant_agent(question):

    answer = run_rag(question)

    return answer