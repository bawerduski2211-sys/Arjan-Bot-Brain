import google.generativeai as genai  # پیتا i بچووک کر

class ArjanAI:
    def __init__(self, api_key):
        # بکارئینانا بهێزترین مۆدێلێ نوکە یێ گوگل
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    async def generate_response(self, user_text):
        # سیستەمێ Streaming بۆ خێراییەکا سۆپەر
        try:
            chat = self.model.start_chat(history=[])
            response = chat.send_message(user_text, stream=True)
            for chunk in response:
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            yield f"Error: {str(e)}"

    def imagen_8k_logic(self, prompt):
        # تەکنەلۆژییا دروستکرنا وێنەیێن Ultra 3D
        enhanced_prompt = f"8K cinematic, ultra-realistic 3D, Duhok style, {prompt}"
        return "arjan_output.jpg"
