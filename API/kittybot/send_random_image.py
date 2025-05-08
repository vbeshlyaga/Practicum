from telebot import TeleBot


bot = TeleBot(token='8090276111:AAHuaYQUFDVstlIzRZDprilF_9uBfzLmMwo')

URL = 'https://cdn2.thecatapi.com/images/3dl.jpg'

chat_id = 742006215
text = 'Вам телеграмма!'
# Отправка сообщения
bot.send_message(chat_id, text)
# Отправка изображения
bot.send_photo(chat_id, URL)