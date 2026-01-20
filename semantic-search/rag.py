# Semantic Retrieval and text generation
# Author: Muhammad Humayun Khan 

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpointEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# load key
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY") 

# creating embeddings
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=api_key
)

# Load Vector DB
vectorstore = FAISS.load_local(
    "faiss_db",
    embeddings,
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# LLM for text generation
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    huggingfacehub_api_token=api_key,
    temperature=0.1,
)
chat_model = ChatHuggingFace(llm=llm)

# prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the question ONLY using the provided context. If the answer is not in the context, say 'I don't know'."),
    ("user", "Context:\n{context}\n\nQuestion: {question}")
])

# Build the Chain using LCEL
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()} | prompt | chat_model | StrOutputParser()
)

# User query
question = "What is the refund policy?"
response = rag_chain.invoke(question)
print(response)

