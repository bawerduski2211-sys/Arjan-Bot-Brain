import google.generativeai as genai
import asyncio

class arjan_engine:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def generate_response(self, prompt):
        try:
            response = self.model.generate_content(prompt, stream=True)
            for chunk in response:
                if chunk.text:
                    yield chunk.text
                    await asyncio.sleep(0.1)
        except Exception as e:
            yield f"error: {str(e)}"
