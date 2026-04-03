import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.rag_pipeline import run_rag


question = input("Ask your question: ")

answer = run_rag(question)

print("\nAnswer:\n")
print(answer)