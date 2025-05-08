from telebot import TeleBot

bot = TeleBot(token='8090276111:AAHuaYQUFDVstlIzRZDprilF_9uBfzLmMwo')

@bot.message_handler(commands=['start'])
def wake_up(message):
    chat = message.chat
    name = chat.first_name
    bot.send_message(chat_id = chat.id, text=f'Спасибо, что включили меня, {name}!')

@bot.message_handler(content_types=['text'])
def say_hi(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id= chat_id, text='Привет, я KittyBot!')


bot.polling()