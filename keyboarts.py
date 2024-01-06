from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from loader import bot

def start_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    key = KeyboardButton("Dushanba")
    key2 = KeyboardButton("Seshanba")
    key3 = KeyboardButton("Chorshanba")
    key4 = KeyboardButton("Payshanba")
    key5 = KeyboardButton("Juma")
    key6 = KeyboardButton("Shanba")
    markup.add(key, key2, key3, key4, key5, key6)
    return markup
