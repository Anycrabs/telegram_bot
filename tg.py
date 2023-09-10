import telebot
from telebot import types

bot = telebot.TeleBot('6273286795:AAE6XmXhR1OLd2kmTd0WZMFkcbZNs_eHoH0')

#   Списки с фильмами
list_comedy = ['1+1', 'Лулу и Бриггс', 'Последний богатырь', 'Голяк', 'Третий лишний', 'Круэлла', ]
list_horror = ['Оно', 'Ходячие мертвецы', 'Очень странные дела', 'Война миров Z', 'Чужой', 'Прочь', ]
list_thriller = ['Остров проклятых', 'Бойцовский клуб', 'Области тьмы', 'Престиж', 'Исчезнувшая', 'Молчание ягнят', ]
list_boevik = ['Гнев человеческий', 'Дэдпул', 'Леон', 'Переводчик', 'Операция Фортуна',
               'Законопослушный гражданин', ]
list_detective = ['Достать ножи', 'Шерлок', 'Черный ящик', 'Шестое чувство', 'Фишер', 'Настоящий детектив', ]
list_fantasy = ['Игра престолов', 'Аватар 2', 'Начало', 'Интерстеллар', 'Мстители Финал',
                'Мстители Война бесконечности', ]

#   Кнопки
btn3 = types.KeyboardButton('Комедия')
btn4 = types.KeyboardButton('Ужасы')
btn5 = types.KeyboardButton('Триллер')
btn6 = types.KeyboardButton('Боевик')
btn7 = types.KeyboardButton('Детектив')
btn8 = types.KeyboardButton('Фантастика')


#   Обработка названий
def films_comedy():
    for item in list_comedy:
        yield item


def films_horror():
    for item1 in list_horror:
        yield item1


def films_triller():
    for item2 in list_thriller:
        yield item2


def films_boevik():
    for item3 in list_boevik:
        yield item3


def films_detective():
    for item4 in list_detective:
        yield item4


def films_fantasy():
    for item5 in list_fantasy:
        yield item5


#   Обработка изображений
def photos_comedy():
    for i in list_comedy:
        yield i


def photos_horror():
    for i2 in list_horror:
        yield i2


def photos_thriller():
    for i3 in list_thriller:
        yield i3


def photos_boevik():
    for i4 in list_boevik:
        yield i4


def photos_detective():
    for i5 in list_detective:
        yield i5


def photos_fantasy():
    for i6 in list_fantasy:
        yield i6


filmtosend_comedy = films_comedy()
filmtosend_horror = films_horror()
filmtosend_triller = films_triller()
filmtosend_boevik = films_boevik()
filmtosend_detective = films_detective()
filmtosend_fantasy = films_fantasy()

phototosend_comedy = photos_comedy()
phototosend_horror = photos_horror()
phototosend_thriller = photos_thriller()
phototosend_boevik = photos_boevik()
phototosend_detective = photos_detective()
phototosend_fantasy = photos_fantasy()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Привет')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет, я бот, который может помочь тебе выбрать фильм",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Привет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton('Погнали')
        markup.add(btn2)
        bot.send_message(message.from_user.id, 'Начнём?', reply_markup=markup)

    elif message.text == 'Погнали':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id,
                         'Давай я предложу тебе парочку фильмов, какой жанр тебе больше нравится?',
                         reply_markup=markup)

    elif message.text == 'Комедия':
        bot.send_message(message.from_user.id, f'{next(filmtosend_comedy)}')
        img = open(f'C:\\forbot\\imagescomedy\\{next(phototosend_comedy)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif message.text == 'Ужасы':
        bot.send_message(message.from_user.id, f'{next(filmtosend_horror)}')
        img2 = open(f'C:\\forbot\\imageshorror\\{next(phototosend_horror)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img2)
    elif message.text == 'Триллер':
        bot.send_message(message.from_user.id, f'{next(filmtosend_triller)}')
        img3 = open(f'C:\\forbot\\imagestriller\\{next(phototosend_thriller)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img3)
    elif message.text == 'Боевик':
        bot.send_message(message.from_user.id, f'{next(filmtosend_boevik)}')
        img4 = open(f'C:\\forbot\\imagesboevik\\{next(phototosend_boevik)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img4)
    elif message.text == 'Детектив':
        bot.send_message(message.from_user.id, f'{next(filmtosend_detective)}')
        img5 = open(f'C:\\forbot\\imagesdetectiv\\{next(phototosend_detective)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img5)
    elif message.text == 'Фантастика':
        bot.send_message(message.from_user.id, f'{next(filmtosend_fantasy)}')
        img6 = open(f'C:\\forbot\\imagesfantasy\\{next(phototosend_fantasy)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img6)


bot.polling(none_stop=True, interval=0)
