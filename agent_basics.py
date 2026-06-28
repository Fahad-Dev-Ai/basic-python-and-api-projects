import warnings
warnings.filterwarnings("ignore")
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool


@tool
def calculator(expression):
    """Useful for solving math problems and calculations. Input should be a mathematical expression like '25 * 48' or '100 / 4'."""
    return str(eval(expression))

@tool
def Celsius_to_Fahrenheit(celsius):
        """this tool is useful for converting temperature from degree celsius to fahrenheit"""
        return str(float(celsius) * 9/5 + 32)
llm = ChatGroq(model="openai/gpt-oss-120b")
search = DuckDuckGoSearchRun()
tools = [search,calculator,Celsius_to_Fahrenheit]
llm_with_tools = llm.bind_tools(tools)
agent = create_react_agent(llm_with_tools, tools)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the current population of Pakistan? Answer in one sentence."}]},
    config={"recursion_limit": 15}
)
print(response["messages"][-1].content)

response2 = agent.invoke(
    {"messages": [{"role":"user","content":"what is '9897*8786' "}]},
config={"recursion_limit" : 15}
)
print(response2["messages"][-1].content)


response3 = agent.invoke(
    {"messages": [{"role":"user","content":"what is 50 degree celsius in fahrenheit"}]},
config={"recursion_limit" : 15}
)
print(response3["messages"][-1].content)