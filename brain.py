import os
import asyncio
from google import genai
from telebot.async_telebot import AsyncTeleBot
from interface import main_keyboard  # بانگکرنا فایلی ئینتەرفەیس

# زانیاریێن گرنگ
BOT_TOKEN = "8386548320:AAF-308Bsm8xunxQKRKiNSPfwTw_5tcxNZQ"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

bot = AsyncTeleBot(BOT_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    welcome_text = "ب خێر بێی بۆ پڕۆژێ Arjan AI! ئەز یێ بەرهەفم بۆ هاریکاریا تە."
    await bot.send_message(message.chat.id, welcome_text, reply_markup=main_keyboard())

@bot.message_handler(func=lambda message: message.text == '🤖 دەربارەی Arjan AI')
async def about_bot(message):
    about_text = "ئەڤ بۆتە پشکەکە ژ پڕۆژێ Arjan AI، یێ هاتیە گەشەپێدان بۆ کارێن ژیرییا دەستکرد."
    await bot.reply_to(message, about_text)

@bot.message_handler(func=lambda message: message.text == '💫 هاریکاری')
async def help_command(message):
    help_text = "تو دشێی هەر پرسیارەکێ ژ من بکەی، ئەز دێ ب ڕێکا Gemini بەرسڤا تە دەم."
    await bot.reply_to(message, help_text)

@bot.message_handler(func=lambda message: True)
async def chat_with_gemini(message):
    try:
        # بکارئینانا مۆدێلا نوو یا گوگل
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=message.text
        )
        await bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error: {e}")

async def main():
    print("🚀 Arjan Bot is Online and Ready!")
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    asyncio.run(main())
