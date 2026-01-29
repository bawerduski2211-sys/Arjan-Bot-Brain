import telebot
import asyncio
from brain import ArjanAI
from telebot.async_telebot import AsyncTeleBot

# کلیلێن تە یێن تایبەت
TOKEN = "8511142007:AAHMKgQmw0g8Vgn_cNSSFJ3-HbsfSXg0SEQ"
GEMINI_KEY = "AIzaSyAzoSTp5o_T3zfqt3FAq-mPkIxmsTsh2Mo"

bot = AsyncTeleBot(TOKEN)
ai_engine = ArjanAI(GEMINI_KEY)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    # نیشاندانا مینی ئەپا فۆڵ شاشە
    markup = telebot.types.InlineKeyboardMarkup()
    web_app = telebot.types.WebAppInfo("https://arjan-ai-pro.vercel.app")
    btn = telebot.types.InlineKeyboardButton("🚀 Arjan AI Pro (Full-Screen)", web_app=web_app)
    markup.add(btn)
    
    welcome = "💎 **Arjan AI Pro 2026** 💎\n\nزیرەکترین تەکنەلۆژیا ل دهۆکێ نوکە ل بەردەستێ تە یە!"
    await bot.send_message(message.chat.id, welcome, reply_markup=markup, parse_mode="MarkdownV2")

@bot.message_handler(func=lambda m: True)
async def handle_chat(message):
    # تەکتیکا Streaming وەڵام پەیڤ ب پەیڤ
    sent_msg = await bot.send_message(message.chat.id, "Searching the neural network... ⚡")
    full_response = ""
    
    async for chunk in ai_engine.generate_response(message.text):
        full_response += chunk
        try:
            # نووکرنا نامێ ب شێوەیەکێ لایڤ
            await bot.edit_message_text(full_response, message.chat.id, sent_msg.message_id)
        except:
            continue

asyncio.run(bot.polling())
