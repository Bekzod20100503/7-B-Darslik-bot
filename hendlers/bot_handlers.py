from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove

from loader import bot
from keyboarts import start_btn

@bot.message_handler(func=lambda message: message.text == "Dushanba")
def reaction_Men_bilan_gaplash(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Dushanba kungi dars jadval\n\n"
                             "1.Adabyot\n"
                              "2.Ona tili\n"
                              "3.Geografiya\n"
                              "4.Tasviriy sanat\n")


@bot.message_handler(func=lambda message: message.text == "Seshanba")
def reaction_Men_bilan_gaplash(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Seshanba kungi dars jadval\n\n"
                             "1.O'zbekiston tarixi\n"
                              "2.Jismoniy tarbiya\n"
                              "3.Chet tili\n"
                              "4.Algebra\n"
                              "5.Jaxon tarixi\n"
                              "6.Ona tili")

@bot.message_handler(func=lambda message: message.text == "Chorshanba")
def reaction_Men_bilan_gaplash(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Seshanba kungi dars jadval\n\n"
                             "1.O'zbekiston tarixi\n"
                              "2.Rus tili\n"
                              "3.Adabiyot\n"
                              "4.Geogirafiya\n"
                              "5.Kimyo\n"
                              "6.Giyometriya")


@bot.message_handler(func=lambda message: message.text == "Payshanba")
def reaction_Men_bilan_gaplash(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Seshanba kungi dars jadval\n\n"
                             "1.Tarbiya\n"
                              "2.Biologiya\n"
                              "3.Fizika\n"
                              "4.Informatika\n"
                              "5.Musiqa\n"
                              "6.Jismoniy tarbiya")


@bot.message_handler(func=lambda message: message.text == "Juma")
def reaction_Men_bilan_gaplash(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Seshanba kungi dars jadval\n\n"
                             "1.Sinf soati\n"
                              "2.Texnologiya\n"
                              "3.Texnologiya\n"
                              "4.Chet tili\n"
                              "5.Biologiya\n"
                              "6.Rus tili")


@bot.message_handler(func=lambda message: message.text == "Shanba")
def reaction_Men_bilan_gaplash(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Seshanba kungi dars jadval\n\n"
                             "1.Kimyo\n"
                              "2.Fizika\n"
                              "3.Algebra\n"
                              "4.Geometriya\n"
                              "5.Ona tili\n"
                              "6.Chet tili")


@bot.message_handler(content_types=['text'])
def reaction_text(message:Message):
    chat_id = message.chat.id
    text = message.text
    bot.send_message(chat_id, "Bu botga yozib bo'lmaydi faqat kinopka bosing !")


