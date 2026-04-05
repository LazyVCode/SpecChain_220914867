"""generates structured specs from personas"""
import json, os
from groq import Groq

def run():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    with open('personas/personas_auto.json', 'r') as f:
        personas = f.read()
        
    prompt = f"Given these personas: {personas}, generate 10 software requirements for Headspace. Format as Markdown. Include Requirement ID, Description, Source Persona, Traceability, and Acceptance Criteria."
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="meta-llama/llama-4-scout-17b-16e-instruct"
    )
    
    os.makedirs('spec', exist_ok=True)
    with open('spec/spec_auto.md', 'w') as f:
        f.write(response.choices[0].message.content)
    print("Auto Specs Generated.")

if __name__ == "__main__": run()
