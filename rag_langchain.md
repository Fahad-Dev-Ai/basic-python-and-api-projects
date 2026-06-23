# RAG System with LangChain

## What it does
A RAG pipeline built with LangChain that splits a document into chunks, stores them in a vector database, retrieves the most relevant chunks based on a user question, and generates an answer using Groq's LLM.

## How it works
1. Split document into chunks using RecursiveCharacterTextSplitter
2. Embed chunks using HuggingFace sentence-transformers
3. Store in ChromaDB vector store
4. Retrieve top 2 relevant chunks for a given question
5. Build prompt with context + question
6. Send to Groq LLM and return answer

## Requirements
- langchain-groq
- langchain-core
- langchain-community
- langchain-huggingface
- langchain-text-splitters
- chromadb
- sentence-transformers

## Setup
1. Install: `pip install langchain-groq langchain-core langchain-community langchain-huggingface langchain-text-splitters chromadb sentence-transformers`
2. Set API key: `$env:GROQ_API_KEY="your_key"`
3. Run: `python rag_langchain.py`
