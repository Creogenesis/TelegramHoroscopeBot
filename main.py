import telebot
from telebot import types
from private import TOKEN
from random import choice

bot = telebot.TeleBot(TOKEN)

first = [
    "Сегодня — идеальный день для новых начинаний.",
    "Оптимальный день для того, чтобы решиться на смелый поступок!",
    "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
    "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
    "Плодотворный день для того, чтобы разобраться с накопившимися делами."
]

second = [
    "Но помните, что даже в этом случае нужно не забывать про", "Если поедете за город, заранее подумайте про",
    "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
    "Если у вас упадок сил, обратите внимание на",
    "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"
]

second_add = [
    "отношения с друзьями и близкими.",
    "работу и деловые вопросы, которые могут так некстати помешать планам.",
    "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
    "бытовые вопросы — особенно те, которые вы не доделали вчера.",
    "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."
]

third = [
    "Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
    "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
    "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
    "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
    "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."
]


@bot.message_handler(content_types=['text'])  # Обработка текстовых сообщений
def get_text_messages(message):
    if message.text.lower() == 'привет':  # Если сообщение в нижнем регистре
        bot.send_message(message.from_user.id,
                         'Привет, сейчас покажу тебе гороскоп на сегодня!')

        keyboard = types.InlineKeyboardMarkup()  # Готовим кнопки
        aries_key = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        taurus_key = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        gemini_key = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        cancer_key = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        leo_key = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        virgo_key = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        libra_key = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        scorpio_key = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        sagittarius_key = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        capricorn_key = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        aquarius_key = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        pisces_key = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')

    elif message.text == '/help':
        bot.send_message(message.from_user.id,
                         'Напиши "Привет"!')
    else:
        bot.send_message(message.from_user.id,
                         'Я тебя не понимаю, напиши /help...')


bot.polling(none_stop=True, interval=0)  # Непрерывная работа бота
