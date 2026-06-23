from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
llm = ChatGroq(
    model="llama-3.1-8b-instant"
)
instruction = ChatPromptTemplate.from_template(
    "you're a coding coach and you have to explain concepts in simple language only for python programming language: {instruction}"
)
chain = instruction | llm
messages = []
while True:
    prompt = input("Enter the prompt: ")
    if prompt == "exit":
        print(messages)
        break

    response = chain.invoke({"instruction": prompt})
    print(response.content)
    messages.append({"question": prompt , "answer": response.content})
