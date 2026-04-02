import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL = "text-embedding-004"
GENERATION_MODEL = "gemini-2.5-flash"
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_KEY_PATH")
VECTOR_COLLECTION = "rag_chunks"

TOP_K = 8

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

DATABASE_NAME = "nimesh-data"