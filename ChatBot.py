import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = 'gpt2-medium'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_response(user_input):
    input_ids = tokenizer.encode(user_input, return_tensors="pt").to(device)
    output = model.generate(input_ids, max_length=60, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[0], skip_special_toekns=True)
    return response

while True:
    user_input = input("Enter your message:")
    if user_input.lower() == "exit":
        break
    reponse = generate_response(user_input)
    print("ChatGPT:", reponse)
    
    