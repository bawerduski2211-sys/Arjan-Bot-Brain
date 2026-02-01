import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from brain import arjan_brain
from interface import main_keyboard

# وەرگرتنا کلیلان ژ سێرڤەری (Environment Variables)
token = os.getenv('TELEGRAM_TOKEN')
gemini_key = os.getenv('GEMINI_API_KEY')

bot = AsyncTeleBot(token)
ai = arjan_brain(gemini_key)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    try:
        markup = main_keyboard()
        text = "💎 <b>arjan ai pro 2026</b> 💎\n\nبوت ب سەرکەفتی کەفتە کار برا! 🚀"
        await bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="HTML")
    except Exception as e:
        print(f"Start error: {e}")

@bot.message_handler(func=lambda m: True)
async def handle_chat(message):
    try:
        # فرێکرنا نامەیەکا دەمکی
        sent_msg = await bot.send_message(message.chat.id, "⚡ arjan ai دبیریت...")
        full_res = ""
        
        # وەرگرتنا بەرسڤا Gemini ب شێوێ Stream
        async for chunk in ai.generate_response(message.text):
            full_res += chunk

        if full_res:
            # نووکرنا نامەیێ ب بەرسڤا تەمام
            await bot.edit_message_text(full_res[:4000], message.chat.id, sent_msg.message_id)
    except Exception as e:
        print(f"Chat error: {e}")

async def run_bot():
    # پاقژکرنا وێبهۆکێن کۆن بۆ نەهێلانا Conflict 409
    await bot.delete_webhook(drop_pending_updates=True)
    print("🚀 Arjan Bot is Online!")
    
    # چاکسازی: ل ڤێرێ مە 'skip_pending_updates' کرە 'skip_pending'
    # چونکی سێرڤەرێ تە پەیڤا درێژ قەبوول نەدکر
    await bot.infinity_polling(timeout=60, skip_pending=True)

if __name__ == "__main__":
    asyncio.run(run_bot())
