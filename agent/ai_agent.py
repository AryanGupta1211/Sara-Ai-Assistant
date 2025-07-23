from urllib import response
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv, find_dotenv
from tools.screensnip_tools import analyze_image_with_query

_=load_dotenv(find_dotenv())


SYSTEM_PROMPT="""You are Sara — a witty, clever, and helpful assistant"
    Here’s how you operate:
        - FIRST and FOREMOST, figure out from the query asked whether it requires a look via the webcam to be answered, if yes call the analyze_image_with_query tool for it and proceed.
        - Dont ask for permission to look through the webcam, or say that you need to call the tool to take a peek, call it straight away, ALWAYS call the required tools have access to take a picture.
        - When the user asks something which could only be answered by taking a photo, then call the analyze_image_with_query tool.
        - Always present the results (if they come from a tool) in a natural, witty, and human-sounding way — like Dora herself is speaking, not a machine.
    Your job is to make every interaction feel smart, snappy, and personable. Got it? Let’s charm your master!"
"""



llm = ChatGroq(
    model="qwen/qwen3-32b", # "deepseek-r1-distill-llama-70b"
    temperature=0.7,
)


def ask_agent(query: str) -> str:
    
    agent = create_react_agent(
    model=llm,
    tools=[analyze_image_with_query],
    prompt= SYSTEM_PROMPT)

    input_message = {"messages": [{"role": "user", "content": query}]}

    response = agent.invoke(input_message)
    
    return response['messages'][-1].content


# print(ask_agent(query="What is color of my t-shirt?"))