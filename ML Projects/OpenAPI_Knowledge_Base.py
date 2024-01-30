import fitz  # PyMuPDF
from openai import OpenAI


client = OpenAI(api_key="")

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return text

def create_knowledge_base(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    knowledge_base = {"Colorado B": text}
    return knowledge_base

def query_knowledge_base(user_input, knowledge_base):
    company_name = "Colorado B" 
    if company_name in knowledge_base:
        knowledge_base_text = knowledge_base[company_name]
        chunk_size = 4000  # Adjust based on your token requirements
        chunks = [knowledge_base_text[i:i+chunk_size] for i in range(0, len(knowledge_base_text), chunk_size)]

        generated_outputs = []

        for chunk in chunks:
            prompt = f"{chunk}\nUser Input: {user_input}\n"
            messages = [{"role": "user", "content": prompt}]

            chat_completion = client.chat.completions.create(
                messages=messages,
                model="gpt-3.5-turbo",
            )

            generated_output = chat_completion.choices[0].message.content.strip()
            generated_outputs.append(generated_output)

        # Combine the generated outputs if needed
        final_output = " ".join(generated_outputs)
        print("Generated Output: ")
        print(final_output)
    else:
        print(f"No information found for {company_name}.")

if __name__ == "__main__":
    pdf_path = " "
    user_input = input("Enter a sentence: ")
    
    knowledge_base = create_knowledge_base(pdf_path)
    
    query_knowledge_base(user_input, knowledge_base)
