# Example Source: https://python.langchain.com/v0.2/docs/integrations/memory/google_firestore/

from dotenv import load_dotenv
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize Local File based Chat History
print("Initializing File based Chat Message History...")
chat_history = FileChatMessageHistory(file_path='session_history')
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# Initialize Chat Model
model = ChatOpenAI()

print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")
