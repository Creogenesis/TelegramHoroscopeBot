import telebot
from telebot import types
from private import TOKEN  # Импорт токена
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
        keyboard.add(aries_key)
        taurus_key = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(taurus_key)
        gemini_key = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(gemini_key)
        cancer_key = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(cancer_key)
        leo_key = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(leo_key)
        virgo_key = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(virgo_key)
        libra_key = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(libra_key)
        scorpio_key = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(scorpio_key)
        sagittarius_key = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(sagittarius_key)
        capricorn_key = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(capricorn_key)
        aquarius_key = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(aquarius_key)
        pisces_key = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(pisces_key)
        bot.send_message(message.from_user.id,
                         text='Выбери свой знак зодиака', reply_markup=keyboard)  # Отображаем кноки

    elif message.text == '/help':
        bot.send_message(message.from_user.id,
                         'Напиши "Привет"!')
    elif message.text == '/info':
        bot.send_message(message.from_user.id,
                         'Мне было в падлу парсить данные с сайтов магов, поэтому'
                         ' у меня есть несколько текстов, из которых я рандомно выбираю'
                         ' предложения и строю будущую реальность (ну типа реальность). Просто выбери свой'
                         ' знак зодиака (можно и не свой - результат всё равно рандомный 😐) и я скажу тебе,'
                         ' чего ожидать в ближайшее время 🤪...')
    else:
        bot.send_message(message.from_user.id,
                         'Я тебя не понимаю, напиши /help...')


@bot.callback_query_handler(func=lambda call: True)  # Обработка нажатий на кнопки
def callback(call):
    if call.data == 'zodiac':
        answer = f'{choice(first)} {choice(second)} {choice(second_add)} {choice(third)}'  # Формирование ответа
        bot.send_message(call.message.chat.id, answer)


bot.polling(none_stop=True, interval=0)  # Непрерывная работа бота
