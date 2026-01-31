from telebot import types # ل ڤێرێ 'from' ب بچووکی بنڤێسە

def main_keyboard():
    # resize_keyboard=True دکەتە د ڕێزەکێ دا و ل سەر مۆبایلێ جوان دیار دبیت
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('🤖 دەربارەی arjan ai')
    itembtn2 = types.KeyboardButton('💫 هاریکاری')
    markup.add(itembtn1, itembtn2)
    return markup