import google.genai as genai
import asyncio

class arjan_brain:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-1.5-flash"

    async def generate_response(self, prompt):
        try:
            # Streaming response
            stream = self.client.models.generate_content_stream(
                model=self.model,
                contents=prompt
            )
            for chunk in stream:
                if chunk.text:
                    yield chunk.text
                    await asyncio.sleep(0.05)
        except Exception as e:
            yield f"❌ error: {e}"