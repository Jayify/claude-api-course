from dotenv import load_dotenv
from anthropic import Anthropic


# Setup
load_dotenv()


# Create API client
client = Anthropic()
model = "claude-haiku-4-5-20251001"


# Helper functions
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


# Main request
def chat(messages):
    # Make a request
    message = client.messages.create(
        model=model,
        max_tokens=100,
        messages=messages
    )
    return message.content[0].text


messages = [] # Define history list


while True:
    user_input = input("Prompt? > ")
    print("> ", user_input)
    add_user_message(messages, user_input)
    response = chat(messages) # Send request to API
    add_assistant_message(messages, response) # Record response in history  
    print("Response > ", response)


