"""generates tests from specs"""
import json, os
from groq import Groq

def run():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    with open('spec/spec_auto.md', 'r') as f:
        specs = f.read()
        
    prompt = f"Given these requirements: {specs}, generate 2 JSON validation tests per requirement. Include test_id, requirement_id, scenario, steps, and expected_result. Output pure JSON."
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        response_format={"type": "json_object"}
    )
    
    os.makedirs('tests', exist_ok=True)
    with open('tests/tests_auto.json', 'w') as f:
        f.write(response.choices[0].message.content)
    print("Auto Tests Generated.")

if __name__ == "__main__": run()
