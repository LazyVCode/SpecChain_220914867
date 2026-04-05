"""automated persona generation pipeline"""
import json, os
from groq import Groq

def run():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = """Analyze Headspace app reviews. Create 5 review groups (themes) and 5 corresponding JSON Personas detailing goals, pain points, context, and constraints. Output pure JSON format."""
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        response_format={"type": "json_object"}
    )
    
    os.makedirs('personas', exist_ok=True)
    with open('personas/personas_auto.json', 'w') as f:
        f.write(response.choices[0].message.content)
    with open('prompts/prompt_auto.json', 'w') as f:
        json.dump({"prompt": prompt}, f)
    print("Auto Personas Generated.")

if __name__ == "__main__": run()
