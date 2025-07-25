import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_response(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant helping with crypto and trading."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
