import streamlit as st
import uuid
from langchain_core.messages import HumanMessage, AIMessage
from backend import chatbot

def generate_thread_id():
    thread_id = str(uuid.uuid4())
    return thread_id

def add_thread(thread_id):
    if thread_id not in st.session_state["thread_list"]:
        st.session_state["thread_list"].append(thread_id)

def reset_state():
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    st.session_state["conversation"] = []
    add_thread(thread_id=thread_id)
    
def generate_config():
    return {"configurable": {"thread_id": st.session_state["thread_id"]}}

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

if "thread_list" not in st.session_state:
    st.session_state["thread_list"] = [] 
    
add_thread(st.session_state["thread_id"])

st.sidebar.title("Langgraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_state()
    
st.sidebar.header("Previous Conversation")

for threads in st.session_state["thread_list"]:
   if st.sidebar.button(str(threads)):
       st.session_state["thread_id"] = threads
       state_snapshot = chatbot.get_state(config=generate_config())
       
       messages = state_snapshot.values.get("messages", [])
       
       conversation = []
       for msg in messages:
           if isinstance(msg, HumanMessage):
               conversation.append({
                   "role": "user",
                   "content": msg.content
               })
           else:
               conversation.append({
                   "role": "assistant",
                   "content": msg.content
               })   
       st.session_state["conversation"] = conversation       
    
for msg in st.session_state["conversation"]:
    with st.chat_message(msg["role"]):
        st.text(msg["content"]) 

prompt = st.chat_input("What's On Your mind Today")

if prompt:
    st.session_state["conversation"].append({"role": "user", "content": prompt})
    with st.chat_message('user'):
        st.text(prompt)
        
    res = chatbot.invoke({"messages": [HumanMessage(content=prompt)]}, config=generate_config())
    ai_message = res["messages"][-1].content
    
    with st.chat_message('assistant'):
        st.text(ai_message)
      
    st.session_state["conversation"].append({"role": "assistant", "content": ai_message})