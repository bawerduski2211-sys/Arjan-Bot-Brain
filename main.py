import os
import telebot
import asyncio
from telebot.async_telebot import AsyncTeleBot
from brain import ArjanAI
# لێرە مێنیۆیا تە ژ فایلا interface بانگ دکەت
from interface import main_keyboard

# وەرگرتنا کلیلان ژ Variables ل سەر Railway
TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_KEY = os.getenv('GEMINI_API_KEY')

bot = AsyncTeleBot(TOKEN)
ai_engine = ArjanAI(GEMINI_KEY)

# فەرمانا Start دگەل مێنیۆیا تە یا نوی
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = main_keyboard() 
    welcome = "💎 **Arjan AI Pro 2026** 💎\n\nخێرهاتی بۆ زیرەکترین بۆت ل کوردستانێ! یەک ژ ڤان بژاردان هەلبژێرە:"
    await bot.send_message(message.chat.id, welcome, reply_markup=markup, parse_mode="Markdown")

# چارەسەرکرنا کلیکێن سەر مێنیۆیێ
@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):
    if call.data == "mode_voice":
        await bot.answer_callback_query(call.id, "سیستەمێ دەنگی هاتە چالاککرن... 🎤")
    elif call.data == "mode_image":
        await bot.answer_callback_query(call.id, "نوکە وێنەیێن 4K بۆ تە ئامادە دکەین... 🎨")
    elif call.data == "mode_studio":
        await bot.answer_callback_query(call.id, "ب خێر بێی بۆ ستۆدیۆیا دیزاینێ... 📸")

# بەرسڤدانا نامەیان ب AI
@bot.message_handler(func=lambda m: True)
async def handle_chat(message):
    sent_msg = await bot.send_message(message.chat.id, "⚡")
    full_response = ""
    async for chunk in ai_engine.generate_response(message.text):
        full_response += chunk
        try:
            await bot.edit_message_text(full_response, message.chat.id, sent_msg.message_id)
        except:
            continue

async def main():
    print("Arjan Bot is Running...")
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    asyncio.run(main())
