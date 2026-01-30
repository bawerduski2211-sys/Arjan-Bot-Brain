from telebot import types

def main_keyboard():
    # دروستکرنا مێنیۆیا پێشکەفتی ب شێوازێ ستوونی
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # پێناسا دوگمەیان ب ناڤێن جوان و سەرنجڕاکێش
    btn1 = types.InlineKeyboardButton("🎤 دانوستاندنا دەنگی یا هەڤالینی", callback_data="mode_voice")
    btn2 = types.InlineKeyboardButton("🎨 وێنەیێن 3D & 4K Ultra", callback_data="mode_image")
    btn3 = types.InlineKeyboardButton("📸 ستۆدیۆیا دیزاینا کەسی", callback_data="mode_studio")
    
    # زێدەکرنا دوگمەیان بۆ مێنیۆیێ
    markup.add(btn1, btn2, btn3)
    
    return markup
