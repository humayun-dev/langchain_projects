# Semantic Retrieval of the context against the query
# Author: Muhammad Humayun Khan

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()
api_key = os.getenv('HUGGINGFACE_API_KEY')

# initialize the same embeddings model
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=api_key
)

# Load the FAISS DB from the local folder
vectorstore = FAISS.load_local(
    "faiss_db", 
    embeddings, 
    allow_dangerous_deserialization=True        # to open the trusted file which i created earlier
)

# user query
query = "What is the refund policy?"

# Similarity search
# k=2 means "find the top 2 most similar pieces of text"
results = vectorstore.similarity_search(query, k=2)

print("\n Search Results:\n")
for i, doc in enumerate(results, 1):
    print(f"{i}. {doc.page_content}")
    print("-" * 30)