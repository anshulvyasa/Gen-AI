import streamlit as st
from langchain_core.messages import HumanMessage
from backend import chatbot

config={"configurable":{"thread_id":"1"}}

if "message-history" not in st.session_state:
    st.session_state["message-history"]=[]
    
for message in st.session_state["message-history"]:
    with st.chat_message(message['role']):
        st.text(message["content"])

prompt=st.chat_input("What's On Your Minds?")

if prompt:
    st.session_state["message-history"].append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.text(prompt)
    
    response=chatbot.invoke({"messages":[HumanMessage(content=prompt)]},config=config)   
    ai_message=response["messages"][-1].content[0]["text"]
    
    st.session_state['message-history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)
