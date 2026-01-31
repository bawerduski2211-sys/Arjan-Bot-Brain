import os
import asyncio
from google import genai
from telebot.async_telebot import AsyncTeleBot

# ل ڤێرە کلیلا تە یا نوو دانی
BOT_TOKEN = "8386548320:AAF-308Bsm8xunxQKRKiNSPfwTw_5tcxNZQ"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

bot = AsyncTeleBot(BOT_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, "سڵاو! ئەز Arjan AI مە، ئەز چەوا دشێم هاریکاریا تە بکەم؟")

@bot.message_handler(func=lambda message: True)
async def chat_with_gemini(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=message.text
        )
        await bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error: {e}")

async def main():
    print("🚀 Arjan Bot is Running with New Library...")
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    asyncio.run(main())
