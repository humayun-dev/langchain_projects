# Smart Document Search Engine using RAG

This project implements a **Semantic Search Engine** enhanced with **Retrieval-Augmented Generation (RAG)**.  
It allows users to query documents based on **meaning**, not keywords, and generates **grounded answers** using retrieved context.

## Why This Project?

Traditional keyword search fails to capture semantic meaning.  
Modern AI systems require **context-aware retrieval** combined with **controlled text generation**.

This project demonstrates a **real-world RAG pipeline**, similar to how systems like ChatGPT retrieve and reason over private knowledge.


## How It Works (Architecture)

Document
↓
Text Chunking
↓
Vector Embeddings (HuggingFace)
↓
FAISS Vector Store
↓
Semantic Similarity Search
↓
Context Injection
↓
LLM Answer Generation (RAG)

