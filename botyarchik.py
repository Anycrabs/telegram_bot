import requests
from bs4 import BeautifulSoup

url = 'https://www.film.ru/online/comedy'
url2 = 'https://www.ivi.ru/movies/comedy'
url3 = 'https://www.kinoafisha.info/rating/movies/comedy/'
responce = requests.get(url3)
xml = BeautifulSoup(responce.text, 'lxml')

#name = xml.find('div', class_="film_list_block").find('div', class_="film_list").find('a', class_="film_list_link").find('strong').text
#print(name)
'''
list_f = []
name1 = xml.find(
    'div', class_="site site-default").find(
    'div', class_="site_columns js-bottom").find(
    'div', class_="site_left").find(
    'div', class_="site_content").find(
    'div', class_="ratings coating-adaptive-main").find(
    'div', class_="ratings_inner grid").find(
    'div', class_="ratings_list movieList grid_cell9").find(
    'div', class_="movieList_item movieItem  movieItem-rating movieItem-position ").find(
    'div', class_="movieItem_info").find_all(
    'a', class_='movieItem_title')
print(name1)
'''
# res = xml.find_all('a', class_="film_list_link")
# print(responce.content)
# def genindexes():
#    for l in range(10):
#        yield l

# genedind = genindexes()
'''
getfilm = xml.find(
    'section', class_="pageSection pageSection_virtual genre__pageSection genre__pageSection_virtual").find(
    'div', class_="pageSection__container").find(
    'div', class_="pageSection__container-inner").find(
    'div', class_="genre__gallery gallery gallery_virtual").find(
    'ul', class_="gallery__list gallery__list_slimPosterBlock gallery__list_type_poster gallery__gallery__list").find(
    'li', class_='gallery__item gallery__item_virtual').find(
    'a', class_="nbl-slimPosterBlock nbl-slimPosterBlock_type_poster nbl-slimPosterBlock_status_subscription nbl-slimPosterBlock_iconStatus_none nbl-slimPosterBlock_available genre__nbl-slimPosterBlock").find(
    'div', class_="nbl-slimPosterBlock__textSection").find(
    'div', class_="nbl-slimPosterBlock__title").find(
    'span', class_="nbl-slimPosterBlock__titleText").text
print(getfilm)
'''
'''
r = requests.get(url)
html = r.text
f = open('test6.html', 'w')
f.write(html)
f.close()
'''
# if  == 'Третий лишний':
# bot.send_message(message.from_user.id, 'Может посмотришь другой жанр?')
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# markup.add(btn4, btn5, btn6, btn7, btn8)
'''
import telebot
import requests
from bs4 import BeautifulSoup
from random import choice

token = '5795844161:AAG9lmzzTQxQ8wJGlUer1dsFE7L8QCvNpgQ'
bot = telebot.TeleBot(token)
@bot.message_handler(comand=['start', 'help'])
def send_welcome(massage):
    welcome_text = 'Привет я знаю много интепесных фактов'
    bot.send_message(massage.chat.id, welcome_text)
@bot.message_handler(commands=['facts'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/')
    html = BeautifulSoup(response, 'lxml')
    facts = html.find_all(class_='p-2 clearfix')
    random_fact = choice(facts)

    bot.send_message(message.chat.id, random_fact.text)

bot.polling()
'''
'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.film.ru/online/action'
responce = requests.get(url)
xml = BeautifulSoup(responce.content, 'lxml')
res = xml.find_all('a', class_="film_list_link")
print(responce.content)

#resp = requests.get("https://www.film.ru/online/action")
#soup = BeautifulSoup(resp.text, 'lxml')

#print(soup.)

r = requests.get('https://3dtoday.ru/3d-models?page=1')
soup = BeautifulSoup(r.text, 'html.parser')

element = soup.find_all('div', class_='film_list_link')
elem_soup = BeautifulSoup(str(element), 'html.parser')
title = elem_soup.find_all('strong')

print(title)

for tag in soup.find_all(True):
    print(tag.name)
'''
# for _ in a:
#    chat_id = message.chat.id
#    bot.send_message(chat_id, _)

# for i in range(len(a)):
#    bot.send_message(chat_id, a[i])