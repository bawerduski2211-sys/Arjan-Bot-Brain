from telebot import types

def main_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('🤖 دەربارەی Arjan AI')
    itembtn2 = types.KeyboardButton('💫 هاریکاری')
    markup.add(itembtn1, itembtn2)
    return markup
