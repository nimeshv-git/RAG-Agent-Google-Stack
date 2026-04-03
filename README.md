

**Restaurant Menu RAG Agent**

A *Retrieval Augmented Generation (RAG) system for querying restaurant menu data using natural language.

The system retrieves relevant menu information from a **vector database** and uses a **large language model** to generate answers grounded in the retrieved data.

It is designed to be **modular and reusable**, making it easy to integrate into **multi-agent workflows or other AI applications**.

---///////..>

# Summary

This project implements a simple end-to-end RAG pipeline:

* JSON menu data is **chunked and embedded**
* Embeddings are stored in **Firestore Vector Search**
* User questions are converted into **query embeddings**
* The most relevant chunks are retrieved
* Gemini generates an answer using the retrieved context

The architecture separates **ingestion, retrieval, and generation**, making the system easy to maintain and extend.

---

# Core Functions

### 1. Data Ingestion

Transforms menu data into searchable embeddings.

```id="ingestion_flow"
JSON → Chunking → Embeddings → Firestore Vector DB
```

Files involved:

```
ingestion/
chunker.py
embedder.py
firestore_writer.py
ingestion_pipeline.py
```

---

### 2. Retrieval

Finds the most relevant menu information for a question.

```
User Query → Query Embedding → Vector Search → Top K Results
```

Files involved:

```
retrieval/
query_embedder.py
vector_search.py
context_builder.py
```

---

### 3. Answer Generation

Uses the retrieved context to generate an answer.

```
Context + Question → Prompt → Gemini → Answer
```

Files involved:

```
generation/
prompt_builder.py
llm_generator.py
```

---

### 4. RAG Pipeline

The complete workflow combining retrieval and generation.

```
User Question
      ↓
Query Embedding
      ↓
Vector Search
      ↓
Context Building
      ↓
Prompt Creation
      ↓
LLM Answer
```

Main pipeline:

```
pipelines/rag_pipeline.py
```

---

# Architecture

```
Menu JSON Data
       │
       ▼
   Chunking
       │
       ▼
   Embeddings
       │
       ▼
Firestore Vector Database
       │
       ▼
 Vector Search
       │
       ▼
 Context Retrieval
       │
       ▼
  Gemini LLM
       │
       ▼
     Answer
```

---

# Multi-Agent Integration

The RAG system is wrapped as an **agent function** so it can be reused inside larger AI systems.

Example:

```python
from agents.restaurant_agent import restaurant_agent

answer = restaurant_agent("Which restaurant sells chicken shawarma?")
print(answer)
```

This design allows the RAG system to be used as:

* a **tool inside agent frameworks**
* part of **multi-agent reasoning pipelines**
* a **backend for chatbots or APIs**

---

# Real World Use Cases

This architecture can be adapted for many retrieval-based AI systems.

Examples:

### Restaurant Search

Query restaurant menus using natural language.

Example:

```
Which restaurant sells chicken shawarma?
```

---

### Customer Support Knowledge Base

Replace menu data with documentation:

```
Product manuals
Support FAQs
Internal guides
```

---

### Compliance or Policy Retrieval

Search regulations or internal policies:

```
What are the AML requirements for customer verification?
```

---

### Enterprise Knowledge Assistants

Allow employees to query internal documents:

```
Company policies
Technical documentation
Operational procedures
```

---

# Running the System

Install dependencies:

```
pip install -r requirements.txt
```

Ingest menu data:

```
python scripts/ingest_json.py
```

Ask questions:

```
python scripts/ask_question.py
```

---

# Key Design Principles

* **Modular pipeline architecture**
* **Separation of ingestion, retrieval, and generation**
* **Reusable agent interface**
* **Compatible with multi-agent systems**
