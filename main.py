import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from brain import ArjanAI
from interface import main_keyboard

# وەرگرتنا کلیلان ژ سێرڤەری
TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_KEY = os.getenv('GEMINI_API_KEY')

bot = AsyncTeleBot(TOKEN)
ai_engine = ArjanAI(GEMINI_KEY)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = main_keyboard() 
    welcome_text = "💎 **Arjan AI Pro 2026** 💎\n\nب خێر بێی! ئەز یێ بەرهەفم."
    await bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(func=lambda m: True)
async def handle_chat(message):
    sent_msg = await bot.send_message(message.chat.id, "⚡...")
    full_response = ""
    
    async for chunk in ai_engine.generate_response(message.text):
        full_response += chunk
        try:
            # نووکرنا بەرسڤێ ل سەر شاشێ
            await bot.edit_message_text(full_response[:4000], message.chat.id, sent_msg.message_id)
        except:
            continue

async def main():
    # پاقژکرنا هەمی پەیوەندیێن کۆن دا تووشی Conflict نەبی
    await bot.delete_webhook(drop_pending_updates=True)
    print("🚀 Arjan Bot is Online!")
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    asyncio.run(main())
