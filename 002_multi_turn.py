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
        max_tokens=1000,
        messages=messages
    )
    return message.content[0].text


messages = [] # Define history list


# Turn 1
add_user_message(messages, "What is quantum computing? Answer in one sentence") # Set first prompt
response = chat(messages) # Send request to API
add_assistant_message(messages, response) # Record response in history

# Turn 2
add_user_message(messages, "Write another sentence")
response = chat(messages)
add_assistant_message(messages, response)

# Display conversation
for item in messages:
    print(item)
