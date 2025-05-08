import requests
from telebot import TeleBot


bot = TeleBot(token='8090276111:AAHuaYQUFDVstlIzRZDprilF_9uBfzLmMwo')

URL = 'https://api.thecatapi.com/v1/images/search'

chat_id = 742006215

# response = requests.get(URL).json()
response = requests.get(URL).json()

random_cat_url = response[0].get('url')

bot.send_photo(chat_id, random_cat_url)