import openai

openai.api_key = "hidden"

raw_data = input("Enter raw data:")

preprocessed_data = raw_data.lower()

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=preprocessed_data,
    max_tokens=50,
    temperature=0.7,
    n=1,
    stop=None
)

generate_output = response.choices[0].text.strip()

print("Generated Output:")
print(generate_output)