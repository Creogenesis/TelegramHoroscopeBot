import telebot
from telebot import types
from private import TOKEN  # Импорт токена
from datetime import *
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
                         'Чтобы начать работу со мной напиши "Привет"!')
    elif message.text == '/info':
        bot.send_message(message.from_user.id,
                         'Я бот-астролог 👵. Каждый день даю астрологический прогноз для всех знаков зодиака 😎.'
                         ' Для этого тебе нужно будет просто выбрать свой знак в меню выбора (Меню появится после '
                         'приветствия) 🧐.')
    else:
        bot.send_message(message.from_user.id,
                         'Я тебя не понимаю, напиши /help.\nЕсли хочешь узнать о том, что я делаю - напиши /info...')


@bot.callback_query_handler(func=lambda call: True)  # Обработка нажатий на кнопки
def callback(call):
    zodiacs = {
        1: ['aries', 'Овнов'],
        2: ['taurus', 'Тельцов'],
        3: ['gemini', 'Близнецов'],
        4: ['cancer', 'Раков'],
        5: ['leo', 'Львов'],
        6: ['virgo', 'Дев'],
        7: ['libra', 'Весов'],
        8: ['scorpio', 'Скорпионов'],
        9: ['sagittarius', 'Стрельцов'],
        10: ['capricorn', 'Козерогов'],
        11: ['aquarius', 'Водолеев'],
        12: ['pisces', 'Рыб']
    }  # Первое значение - для формирования ссылки, второе - для формирования ответа

    url = f'https://1001goroskop.ru/?znak={zodiacs[int(call.data[0])]}'  # URL адрес
    answer = ''
    request = requests.get(url)  # Отправлямем GET запрос
    soup = BeautifulSoup(request.text, 'html.parser')
    data = soup.find('p')  # Ищем обзац, где написан нужный текст (он там один, поэтому аргументов больше нет)
    for string in data:
        answer += string  # Формируем ответ
    bot.send_message(call.message.chat.id,
                     f'Гороскоп для {zodiacs[int(call.data)][1]} на {datetime.now().date()}')
    bot.send_message(call.message.chat.id, answer)


bot.polling(none_stop=True, interval=0)  # Непрерывная работа бота
