from pyrogram import Client

api_id = 24959940
api_hash = '1c2a8482c0078c357476b4c6909cef66'

# Создаём программный клиент, передаём в него
# имя сессии и данные для аутентификации в Client API
app = Client('my_account', api_id, api_hash)

app.start()
# Отправляем сообщение
# Первый параметр — это id чата (тип int) или имя получателя (тип str).
# Зарезервированное слово 'me' означает собственный аккаунт отправителя.
app.send_message('me', 'Привет')
app.stop()