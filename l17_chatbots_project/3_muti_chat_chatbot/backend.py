from dotenv import load_dotenv
from typing import TypedDict,Annotated
from langchain_core.messages import AIMessage,HumanMessage,BaseMessage
from pydantic import BaseModel,Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

class StructeredOutput(BaseModel):
    content:str = Field(description="The Reply For The Prompt")

llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
structed_llm=llm.with_structured_output(StructeredOutput)

def chat_node(state:ChatState):
    messages=state["messages"]
    llm_output=structed_llm.invoke(messages)
    return {"messages":[AIMessage(content=llm_output.content)]}

# Define Graph
graph=StateGraph(ChatState)

# Define The Nodes
graph.add_node("chat_node",chat_node)

# Define The Edges
graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

# Compile The Graph
chatbot=graph.compile(checkpointer=InMemorySaver())





    