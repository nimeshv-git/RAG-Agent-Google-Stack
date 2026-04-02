from retrieval.query_embedder import embed_query
from retrieval.vector_search import search_vectors


query = "Chicken Shawarma"

embedding = embed_query(query)

results = search_vectors(embedding)

for doc in results:
    print(doc.to_dict())