import google.generativeai as genai
import os

class ArjanAI:
    def __init__(self, api_key):
        # ڕێکخستنا کلیلێ ب ستانداردێ جیهانی
        genai.configure(api_key=api_key)
        
        # ب کارئینانا مۆدێلێ Flash کو خێراترینە بۆ تێلیگرامی و ئاریشەیا 404 ناهێلیت
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def generate_response(self, prompt):
        """
        ئەڤ پشکە بەرسڤێ ب شێوازێ پارچە پارچە (بيت بيت) دروست دکەت
        """
        try:
            # چالاککرنا Streaming دا کو بۆت وەک مرۆڤی بنڤیسیت
            response = self.model.generate_content(prompt, stream=True)
            
            # ڤەگوهۆستنا پارچەیێن بەرسڤێ بۆ فایلێ main.py
            for chunk in response:
                if chunk.text:
                    yield chunk.text
                    
        except Exception as e:
            # نیشاندانا خەلەتییێ ب شێوازەکێ جوان ئەگەر ئاریشە هەبیت
            yield f"⚠️ ببورە برا، د مێشکێ من دا ئاریشەیەک چێبوو: {str(e)}"
