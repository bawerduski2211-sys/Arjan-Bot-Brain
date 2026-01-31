import google.generativeai as genai

class ArjanAI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        # مۆدێل هاتە گوهۆڕین بۆ gemini-1.5-flash دا خەلەتییا 404 نەمینیت
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def generate_response(self, prompt):
        # بکارئینانا Streaming بۆ بەرسڤدانەکا خێرا و پیت ب پیت
        response = self.model.generate_content(prompt, stream=True)
        for chunk in response:
            if chunk.text:
                yield chunk.text
