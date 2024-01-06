from telebot.types import Message

from keyboarts import start_btn

from loader import bot


@bot.message_handler(commands=['start'])
def reaction_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Assalomu alekom, {message.from_user.full_name} Bu bot da 7-B sinf dars jadvali bor sinab ko'ring", reply_markup=start_btn())