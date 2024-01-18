import telebot
from telebot import types

bot = telebot.TeleBot('6377795458:AAF8vgA_cNDpOqUPcn2grToLTdXkjb1Kg3E')

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

btn2 = types.KeyboardButton('Погнали')
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

btn1 = types.KeyboardButton('Привет')
@bot.message_handler(commands=['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup1.add(btn1)
    bot.send_message(message.chat.id, "Привет, я бот, который может помочь тебе выбрать фильм",
                     reply_markup=markup1)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text:
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup2.add(btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, "Выбери жанр фильма", reply_markup=markup2)

    elif message.text == 'Комедия':
        img = open(f'.\\{next(phototosend_comedy)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.from_user.id, f'{next(filmtosend_comedy)}')
    elif message.text == 'Ужасы':
        img2 = open(f'.\\{next(phototosend_horror)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img2)
        bot.send_message(message.from_user.id, f'{next(filmtosend_horror)}')
    elif message.text == 'Триллер':
        img3 = open(f'.\\{next(phototosend_thriller)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img3)
        bot.send_message(message.from_user.id, f'{next(filmtosend_triller)}')
    elif message.text == 'Боевик':
        img4 = open(f'.\\{next(phototosend_boevik)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img4)
        bot.send_message(message.from_user.id, f'{next(filmtosend_boevik)}')
    elif message.text == 'Детектив':
        img5 = open(f'.\\f{next(phototosend_detective)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img5)
        bot.send_message(message.from_user.id, f'{next(filmtosend_detective)}')
    elif message.text == 'Фантастика':
        img6 = open(f'.\\{next(phototosend_fantasy)}.jpg', 'rb')
        bot.send_photo(message.chat.id, img6)
        bot.send_message(message.from_user.id, f'{next(filmtosend_fantasy)}')


bot.polling(none_stop=True, interval=0)
