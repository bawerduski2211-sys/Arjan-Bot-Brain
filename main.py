import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from brain import arjan_engine
from interface import main_keyboard

token = os.getenv('TELEGRAM_TOKEN')
gemini_key = os.getenv('GEMINI_API_KEY')

bot = AsyncTeleBot(token)
ai = arjan_engine(gemini_key)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    try:
        markup = main_keyboard()
        text = "💎 arjan ai pro 2026 💎\n\nب خێر بێی برا، ئەز یێ بەرهەفم!"
        await bot.send_message(message.chat.id, text, reply_markup=markup)
    except Exception as e:
        print(f"error: {e}")

@bot.message_handler(func=lambda m: True)
async def handle_chat(message):
    try:
        await bot.send_chat_action(message.chat.id, 'typing')
        sent_msg = await bot.send_message(message.chat.id, "⚡...")
        
        full_res = ""
        count = 0

        async for chunk in ai.generate_response(message.text):
            full_res += chunk
            count += 1
            if count % 5 == 0:
                try:
                    await bot.edit_message_text(full_res[:4000], message.chat.id, sent_msg.message_id)
                except:
                    continue

        await bot.edit_message_text(full_res[:4000], message.chat.id, sent_msg.message_id)
    except Exception as e:
        print(f"chat error: {e}")

async def run_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    print("🚀 bot is online!")
    await bot.infinity_polling(timeout=60, allowed_updates=['message'])

if __name__ == "__main__":
    asyncio.run(run_bot())
