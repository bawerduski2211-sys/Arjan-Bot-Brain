import google.generativeai as genai

class ArjanAI:
    def __init__(self, api_key):
        # بکارئینانا بهێزترین مۆدێلێ ٢٠٢٦ێ یێ گووڵ
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-3-pro-preview')

    async def generate_response(self, user_text):
        # سیستەمێ Streaming بۆ خێراییەکا سۆپەر
        chat = self.model.start_chat(history=[])
        response = chat.send_message(user_text, stream=True)
        for chunk in response:
            yield chunk.text

    def imagen_8k_logic(self, prompt):
        # تەکنەلۆژییا دروستکرنا وێنەیێن Ultra 3D
        enhanced_prompt = f"8K cinematic, ultra-realistic 3D, Duhok style, {prompt}"
        # ل ڤێرێ کۆدێ وێنەی دگەل Imagen 3
        return "arjan_output.jpg"
