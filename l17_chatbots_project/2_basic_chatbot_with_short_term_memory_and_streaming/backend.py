from dotenv import load_dotenv
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage,HumanMessage
from typing import TypedDict,Annotated
from langgraph.graph.message import add_messages

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
message=llm.invoke("What is The Capital of India?")


class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]
    
    
def chat_node(state:ChatState)->ChatState:
    message=state["messages"]
    response=llm.invoke(message)
    
    return {"messages":response}


# Define The Graph
graph=StateGraph(ChatState)

# Add The Nodes
graph.add_node("chat_node",chat_node)

# Add The Edges
graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)


chatbot=graph.compile(checkpointer=InMemorySaver())    