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
def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }

    if system:
        params["system"] = system
    
    # Make a request
    message = client.messages.create(**params);
    return message.content[0].text


messages = [] # Define history list
system_prompt = """
    You are a math tutor. Do not directly answer student's questions but 
    guide them to the answer step by step.
"""
temperature=0.1 # 0 is more deterministic, 1 is more creative


while True:
    user_input = input("Prompt? > ")
    print("> ", user_input)
    add_user_message(messages, user_input)

    response = chat(messages, system=system_prompt, temperature=temperature)

    add_assistant_message(messages, response)
    print("Response > ", response.content[0].text)

