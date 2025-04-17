import json
from openai import OpenAI
from utils.config import OPENAI_API_KEY

def ask_gpt(prompt: str) -> str:
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=OPENAI_API_KEY
    )

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt}
            ],
            model="gpt-4o",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )
        return response.choices[0].message.content

    except Exception as e:
        return json.dumps({"error": str(e)})
