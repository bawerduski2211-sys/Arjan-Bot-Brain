import os
import telebot
import asyncio
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from brain import ArjanAI

# وەرگرتنا کلیلان ژ سێرڤەری
TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_KEY = os.getenv('GEMINI_API_KEY')

bot = AsyncTeleBot(TOKEN)
ai_engine = ArjanAI(GEMINI_KEY)

# --- بەشێ مێنیۆیا تە یا نوی ---
def main_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("🎤 دانوستاندنا دەنگی یا هەڤالینی", callback_data="mode_voice")
    btn2 = types.InlineKeyboardButton("🎨 وێنەیێن 3D & 4K Ultra", callback_data="mode_image")
    btn3 = types.InlineKeyboardButton("📸 ستۆدیۆیا دیزاینا کەسی", callback_data="mode_studio")
    markup.add(btn1, btn2, btn3)
    return markup

# --- فەرمانا Start ---
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = main_keyboard() 
    welcome = "💎 **Arjan AI Pro 2026** 💎\n\nخێرهاتی بۆ زیرەکترین بۆت ل کوردستانێ! یەک ژ ڤان بژاردان هەلبژێرە:"
    await bot.send_message(message.chat.id, welcome, reply_markup=markup, parse_mode="Markdown")

# --- بەرسڤدانا نامەیان ب AI ---
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

# --- کارپێکرنا پڕۆژەی ---
async def main():
    print("Arjan Bot is Running...")
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    asyncio.run(main())
