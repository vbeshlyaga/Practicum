import telebot

# Укажите токен, 
# который вы получили от @Botfather при создании бот-аккаунта:
bot = telebot.TeleBot(token='8090276111:AAHuaYQUFDVstlIzRZDprilF_9uBfzLmMwo')
# Укажите id своего аккаунта в Telegram:
chat_id = 742006215
message = 'Вам телеграмма!'
# Вызываем метод send_message, с помощью этого метода отправляются сообщения:
bot.send_message(chat_id, message)