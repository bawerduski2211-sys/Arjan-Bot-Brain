import os
import telebot
import asyncio
from brain import ArjanAI
from telebot.async_telebot import AsyncTeleBot

# لێرە کۆد دێ کلیلان ژ بەشێ Variables وەرگریت
TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_KEY = os.getenv('GEMINI_API_KEY')

bot = AsyncTeleBot(TOKEN)
ai_engine = ArjanAI(GEMINI_KEY)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    # لینکێ مینی ئەپا تە
    web_app = telebot.types.WebAppInfo("https://arjan-ai-pro.vercel.app")
    btn = telebot.types.InlineKeyboardButton("🚀 Arjan AI Pro (Full-Screen)", web_app=web_app)
    markup.add(btn)
    
    welcome = "💎 **Arjan AI Pro 2026** 💎\n\nزیرەکترین تەکنەلۆژیا ل دهۆکێ نوکە ل بەردەستێ تە یە!"
    await bot.send_message(message.chat.id, welcome, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(func=lambda m: True)
async def handle_chat(message):
    sent_msg = await bot.send_message(message.chat.id, "Searching the neural network... ⚡")
    full_response = ""
    
    async for chunk in ai_engine.generate_response(message.text):
        full_response += chunk
        try:
            await bot.edit_message_text(full_response, message.chat.id, sent_msg.message_id)
        except:
            continue

# ڕێکا درستا کارپێکرنێ ل سەر سێرڤەر
async def main():
    print("Arjan Bot is Running...")
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    asyncio.run(main())
