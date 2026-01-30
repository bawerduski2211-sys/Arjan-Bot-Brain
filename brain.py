import google.generativeai as genai

class ArjanAI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    async def generate_response(self, prompt):
        # بکارئینانا Streaming بۆ هندێ پیت ب پیت بەرسڤێ بدەت
        response = self.model.generate_content(prompt, stream=True)
        for chunk in response:
            if chunk.text:
                yield chunk.text
