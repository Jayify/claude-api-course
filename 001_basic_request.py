from dotenv import load_dotenv
from anthropic import Anthropic


# Setup
load_dotenv()


# Create API client
client = Anthropic()
model = "claude-haiku-4-5-20251001"


# Make a request
message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)


# Get output message
print(message.content[0].text)