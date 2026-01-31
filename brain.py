from google import genai
import asyncio

class ArjanAI:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    async def generate_response(self, prompt):
        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            words = response.text.split()
            for i in range(0, len(words), 5):
                yield " ".join(words[i:i+5]) + " "
                await asyncio.sleep(0.1)
        except Exception as e:
            yield f"خەلەتیەک چێبوو: {str(e)}"