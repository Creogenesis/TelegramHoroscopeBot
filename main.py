import telebot
from telebot import types
from private import TOKEN  # Импорт токена
import requests  # Импорт модулей для парсинга
from bs4 import BeautifulSoup


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])  # Обработка текстовых сообщений
def get_text_messages(message):
    if message.text.lower() == 'привет':  # Если сообщение в нижнем регистре
        bot.send_message(message.from_user.id,
                         'Привет, сейчас покажу тебе гороскоп на сегодня!')

        keyboard = types.InlineKeyboardMarkup()  # Готовим кнопки
        aries_key = types.InlineKeyboardButton(text='Овен', callback_data=1)
        keyboard.add(aries_key)
        taurus_key = types.InlineKeyboardButton(text='Телец', callback_data=2)
        keyboard.add(taurus_key)
        gemini_key = types.InlineKeyboardButton(text='Близнецы', callback_data=3)
        keyboard.add(gemini_key)
        cancer_key = types.InlineKeyboardButton(text='Рак', callback_data=4)
        keyboard.add(cancer_key)
        leo_key = types.InlineKeyboardButton(text='Лев', callback_data=5)
        keyboard.add(leo_key)
        virgo_key = types.InlineKeyboardButton(text='Дева', callback_data=6)
        keyboard.add(virgo_key)
        libra_key = types.InlineKeyboardButton(text='Весы', callback_data=7)
        keyboard.add(libra_key)
        scorpio_key = types.InlineKeyboardButton(text='Скорпион', callback_data=8)
        keyboard.add(scorpio_key)
        sagittarius_key = types.InlineKeyboardButton(text='Стрелец', callback_data=9)
        keyboard.add(sagittarius_key)
        capricorn_key = types.InlineKeyboardButton(text='Козерог', callback_data=10)
        keyboard.add(capricorn_key)
        aquarius_key = types.InlineKeyboardButton(text='Водолей', callback_data=11)
        keyboard.add(aquarius_key)
        pisces_key = types.InlineKeyboardButton(text='Рыбы', callback_data=12)
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
    zodiacs = {
        1: 'aries',
        2: 'taurus',
        3: 'gemini',
        4: 'cancer',
        5: 'leo',
        6: 'virgo',
        7: 'libra',
        8: 'scorpio',
        9: 'sagittarius',
        10: 'capricorn',
        11: 'aquarius',
        12: 'pisces'
    }

    url = f'https://1001goroskop.ru/?znak={zodiacs[int(call.data)]}'  # URL адрес
    answer = ''
    request = requests.get(url)  # Отправлямем GET запрос
    soup = BeautifulSoup(request.text, 'html.parser')
    data = soup.find('p')  # Ищем обзац, где написан нужный текст (он там один, поэтому аргументов больше нет)
    for string in data:
        answer += string  # Формируем ответ
    bot.send_message(call.message.chat.id, 'Гороскоп для выбранного знака на сегодня:')  # Добавить знак зодиака
    bot.send_message(call.message.chat.id, answer)


bot.polling(none_stop=True, interval=0)  # Непрерывная работа бота
