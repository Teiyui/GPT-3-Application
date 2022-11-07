import os
import openai

# Set your OpenAI API key via environmental variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Generate a prompt
gpt_prompt = "Generate a sentence about kitchen."

# Call the GPT-3 interface and get its response
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=gpt_prompt,
  temperature=0.5,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response['choices'][0]['text'])
