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
    st.session_state["message-history"].append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    def generate_response():
       for message_chunk, meta_data in chatbot.stream(
        {"messages": [HumanMessage(content=prompt)]},
        config=config,
        stream_mode="messages"
        ):

          content = message_chunk.content

          if (
            isinstance(content, list)
            and len(content) > 0
            and "text" in content[0]
           ):
              yield content[0]["text"]

    with st.chat_message("assistant"):
        ai_message = st.write_stream(generate_response())

    st.session_state["message-history"].append(
        {"role": "assistant", "content": ai_message}
    )