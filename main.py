import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from brain import arjan_brain
from interface import main_keyboard

token = os.getenv("TELEGRAM_TOKEN")
gemini_key = os.getenv("GEMINI_API_KEY")

bot = AsyncTeleBot(token)
ai = arjan_brain(gemini_key)

# Start command
@bot.message_handler(commands=["start"])
async def start(message):
    try:
        markup = main_keyboard()
        text = "💎 <b>arjan ai pro 2026</b> 💎\n\nبوت بە سەركەوتووي كار دەكات 🚀"
        await bot.send_message(
            chat_id=message.chat.id,
            text=text,
            reply_markup=markup,
            parse_mode="HTML"
        )
    except Exception as e:
        print("START ERROR:", e)

# Click buttons & chat handling
@bot.message_handler(func=lambda m: m.text)
async def handle_buttons(message):
    text = message.text

    if text == '🤖 دەربارەی arjan ai':
        reply = "🤖 من arjan ai‌م، هه‌موو پرسیارت ده‌توانم وەڵام بدەم!"
        await bot.send_message(message.chat.id, reply)

    elif text == '💫 هاریکاری':
        reply = "💫 ئەڤ هاریکاریه‌ی تۆ ده‌توانیت لێره‌ بپرسیت، من یارمەتیدەم!"
        await bot.send_message(message.chat.id, reply)

    else:
        # AI chat streaming
        sent = await bot.send_message(message.chat.id, "⚡ arjan ai دبيريت...")
        full = ""
        async for part in ai.generate_response(message.text):
            full += part
        await bot.edit_message_text(full[:4000], message.chat.id, sent.message_id)

# Run bot
async def run_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    print("🚀 Arjan Bot is Online!")
    await bot.infinity_polling(skip_pending=True, timeout=30)

if __name__ == "__main__":
    asyncio.run(run_bot())