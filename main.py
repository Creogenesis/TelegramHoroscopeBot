import telebot
from private import TOKEN
from random import choice


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])  # Обработка текстовых сообщений
def get_text_messages(message):
    if message.text.lower() == 'привет':  # Если сообщение в нижнем регистре
        bot.send_message(message.from_user.id,
                         'Привет, сейчас покажу тебе гороскоп на сегодня!')
    elif message.text == '/help':
        bot.send_message(message.from_user.id,
                         'Напиши "Привет"!')
    else:
        bot.send_message(message.from_user.id,
                         'Я тебя не понимаю, напиши /help...')



