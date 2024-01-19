import os
from openai import OpenAI

client = OpenAI(
    api_key="hidden"
)

raw_data = input("Enter a sentence to be translated to french: ")

preprocessed_data = raw_data.lower()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            ##Prompt for GPT to use
            "content": f"Translate this sentence to French: {preprocessed_data}",
        }
    ],
    model="gpt-3.5-turbo",
)

generate_output = chat_completion.choices[0].message.content.strip()
print("Generated Output in french: ")
print(generate_output)