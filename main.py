import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from brain import arjan_brain
from interface import main_keyboard

token = os.getenv('TELEGRAM_TOKEN')
gemini_key = os.getenv('GEMINI_API_KEY')

bot = AsyncTeleBot(token)
ai = arjan_brain(gemini_key)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    try:
        markup = main_keyboard()
        text = "💎 arjan ai pro 2026 💎\n\nبوت کەفتە کار برا!"
        await bot.send_message(message.chat.id, text, reply_markup=markup)
    except Exception as e:
        print(f"error: {e}")

@bot.message_handler(func=lambda m: True)
async def handle_chat(message):
    try:
        sent_msg = await bot.send_message(message.chat.id, "⚡...")
        full_res = ""
        async for chunk in ai.generate_response(message.text):
            full_res += chunk
            # Edit message logic here
        await bot.edit_message_text(full_res[:4000], message.chat.id, sent_msg.message_id)
    except:
        pass

async def run_bot():
    # ئەڤ دێڕە گەلەک گرنگە بۆ نەهێلانا Conflict
    await bot.delete_webhook(drop_pending_updates=True)
    print("🚀 Arjan Bot is Online!")
    await bot.infinity_polling(timeout=60)

if __name__ == "__main__":
    asyncio.run(run_bot())
