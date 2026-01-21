# A conversational AI chatbot that remembers past messages, uses prompt templates, and adjusts responses based on conversation context.
# Author: Muhammad Humayun Khan

import streamlit as st
from chatbot.chains import get_chat_chain
import uuid

st.set_page_config(page_title="Memory-Aware Chatbot")

st.title("Memory-Aware AI Chatbot")
st.caption("Groq + LangChain + Streamlit")

# Initialize session state
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# Load chat chain
if "chat_chain" not in st.session_state:
    st.session_state.chat_chain = get_chat_chain()

chat_chain = st.session_state.chat_chain

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Invoke chatbot
    response = st.session_state.chat_chain.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": st.session_state.session_id}}
    )

    bot_reply = response.content

    # Show bot message
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
