# Project is about semantic search in the provided data and text generation
# ingest.py upload file, creating chunks, embeddings and store the vectors in the local db
# search.py is only for the semantic search
# rag.py have the RAG pipeline as semantic search and retrieval 
# the steps are to load the document, split the text and create chunks, create embeddings and then store in the database,finally match
# against the query

# Author: Muhammad Humayun Khan

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Load the secrets from the .env file
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")
# Step 1: load the file, it will read and will wrap into a document object (text + metadata)
loader = TextLoader('data/company-policy.txt')
document = loader.load()

# chunking
# split the document text as LLMs can't read more text at once so chunks is a better way to understand for the LLMs
# RecursiveCharacterTextSplitter removes the double new lines, single line, spaces etc
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,       # chunk size is 200
    chunk_overlap = 20      # overlap ensures context isn't lost and the next chunk should have 20 characters with previous one
)
chunks = text_splitter.split_documents(document)

# creating embeddings using the Inference API key
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=api_key
)

# vectors storage in FAISS, from_documents automatically converts the chunks into the embeddings rather than manual
vectorstore = FAISS.from_documents(chunks,embeddings)
vectorstore.save_local("faiss_db")
print("Documents embedded and stored successfully")


