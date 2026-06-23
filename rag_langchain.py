from langchain_core.tools import retriever
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

paragraph = """
Python is a high-level programming language known for its simplicity and readability.
It was created by Guido van Rossum and first released in 1991.
Python supports multiple programming paradigms including procedural, object-oriented, and functional programming.
It has a large standard library and an active community that contributes thousands of third-party packages.
Python is widely used in web development, data science, automation, and artificial intelligence.
Many companies like Google, Netflix, and Instagram use Python in their technology stack.
Python's syntax is designed to be intuitive and its code is often described as executable pseudocode.
The language emphasizes code readability and allows programmers to express concepts in fewer lines of code.
Python has a dynamic type system and automatic memory management.
It also supports multiple programming paradigms and has a comprehensive standard library.
"""
splitter = RecursiveCharacterTextSplitter(
chunk_size = 120,
chunk_overlap = 10
)
embeddings = HuggingFaceEmbeddings(model_name ="all-MiniLM-L6-v2" )
docs = splitter.create_documents([paragraph])
vectorstore = Chroma.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs = {"k":2})
llm = ChatGroq(model = "llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_template("""
answer this only from the context given only
context : {context}
question : {question}

""")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

answer = chain.invoke("what is python used for")
print(answer)