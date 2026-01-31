import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from brain import ArjanAI
from interface import main_keyboard

# وەرگرتنا کلیلان ژ Variables یێن سێرڤەری (پشتڕاست بە ناڤ د وەک هەڤ بن)
TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_KEY = os.getenv('GEMINI_API_KEY')

bot = AsyncTeleBot(TOKEN)
ai_engine = ArjanAI(GEMINI_KEY)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = main_keyboard() 
    welcome_text = "💎 **Arjan AI Pro 2026** 💎\n\nب خێر بێی! ئەز یێ ل ڤێرەم دا هاریکاریا تە بکەم."
    await bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(func=lambda m: True)
async def handle_chat(message):
    # نیشاندانا نیشانا (typing) دا کو بەرهەڤی دیار بیت
    await bot.send_chat_action(message.chat.id, 'typing')
    
    sent_msg = await bot.send_message(message.chat.id, "⚡...")
    full_response = ""
    
    try:
        async for chunk in ai_engine.generate_response(message.text):
            full_response += chunk
            # ئیدیت کرنا پەیامێ ب شێوەیێ (Streaming) وەک ChatGPT
            try:
                if len(full_response.strip()) > 0:
                    await bot.edit_message_text(full_response, message.chat.id, sent_msg.message_id)
            except:
                continue
    except Exception as e:
        print(f"Error in chat: {e}")
        await bot.edit_message_text("ببورە، ئاریشەیەک د سێرڤەری دا چێبوو.", message.chat.id, sent_msg.message_id)

async def main():
    # ئەڤ فەرمانە گەلەک گرنگە دا کو هەمی ئەو پەیامێن ل هیڤیێ ماین (Pending) ژێببەت و Conflict چێنەبیت
    await bot.delete_webhook(drop_pending_updates=True)
    print("🚀 Arjan Bot is Running Successfully on Railway...")
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    asyncio.run(main())
