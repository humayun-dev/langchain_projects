# prompt template logic

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

def get_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "You are a friendly AI assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])