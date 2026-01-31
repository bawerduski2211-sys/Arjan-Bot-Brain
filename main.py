import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from brain import arjan_brain
from interface import main_keyboard

token = os.getenv("TELEGRAM_TOKEN")
gemini_key = os.getenv("GEMINI_API_KEY")

bot = AsyncTeleBot(token)
ai = arjan_brain(gemini_key)

@bot.message_handler(commands=["start"])
async def start(message):
    markup = main_keyboard()
    text = "💎 arjan ai pro 2026 💎\n\nبوت بە سەركەوتووي كار دەكات 🚀"
    await bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda m: m.text and not m.text.startswith("/"))
async def chat(message):
    sent = await bot.send_message(message.chat.id, "⚡ arjan ai دبيريت...")
    full = ""

    async for part in ai.generate_response(message.text):
        full += part

    await bot.edit_message_text(full[:4000], message.chat.id, sent.message_id)

async def run_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    print("🚀 Arjan Bot is Online!")
    await bot.infinity_polling(skip_pending=True, timeout=30)

if __name__ == "__main__":
    asyncio.run(run_bot())