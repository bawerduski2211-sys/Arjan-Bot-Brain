import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from brain import ArjanAI
from interface import main_keyboard

# وەرگرتنا کلیلان ژ سێرڤەری (Environment Variables)
TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_KEY = os.getenv('GEMINI_API_KEY')

# دەستپێکرنا بۆتی ب شێوازێ Async (بۆ لەزاتییا زۆر)
bot = AsyncTeleBot(TOKEN)
ai_engine = ArjanAI(GEMINI_KEY)

# فەرمانا Start و نیشاندانا مێنیۆیا پێشکەفتی
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = main_keyboard() 
    welcome_text = (
        "💎 **Arjan AI Pro 2026** 💎\n\n"
        "ب خێر بێی بۆ زیرەکترین بۆت ل کوردستانێ!\n"
        "ئەز دشێم ب شێوازێ **پیت ب پیت** بەرسڤا تە بدەم."
    )
    await bot.send_message(
        message.chat.id, 
        welcome_text, 
        reply_markup=markup, 
        parse_mode="Markdown"
    )

# بەرسڤدانا نامەیان ب شێوازێ (بيت بيت) وەک ChatGPT
@bot.message_handler(func=lambda m: True)
async def handle_chat(message):
    # نیشانەکا لایڤ (Flash) بۆ دەستپێکا بەرسڤێ
    sent_msg = await bot.send_message(message.chat.id, "⚡...")
    full_response = ""
    
    # وەرگرتنا بەرسڤێ پارچە پارچە ژ مێشکێ Gemini
    async for chunk in ai_engine.generate_response(message.text):
        full_response += chunk
        try:
            # نووکرنا نامەیێ ل تێلیگرامی دا کو پیت ب پیت دیار بیت
            await bot.edit_message_text(
                full_response, 
                message.chat.id, 
                sent_msg.message_id
            )
        except Exception:
            # بۆ ڕێگری ل ڕاوەستانا بۆتی دەما گوهۆڕین گەلەک خێرا بن
            continue

async def main():
    print("🚀 Arjan Bot is Running (Live Streaming Mode)...")
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    asyncio.run(main())
