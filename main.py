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
        # هه‌ر پەيامێ تر بۆ AI
        sent = await bot.send_message(message.chat.id, "⚡ arjan ai دبيريت...")
        full = ""
        async for part in ai.generate_response(message.text):
            full += part
        await bot.edit_message_text(full[:4000], message.chat.id, sent.message_id)