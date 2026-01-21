# LLM chain assembly

from chatbot.llm import get_llm
from chatbot.prompt import get_prompt
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# store the messages
store = {}

# check if the user is new or have the history
def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# connecting the user prompt with the history/record
def get_chat_chain():
    chain = get_prompt() | get_llm()

    return RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key = "input",
        history_messages_key = "history"
    )

