import requests

response = requests.get('https://swapi.dev/api/starships/9/', verify=False)
response = response.text
# Напечатаем в терминале содержимое ответа сервера...
print(response)
# ...и его тип
print(type(response))