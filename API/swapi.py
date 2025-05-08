import requests
from pprint import pprint

response = requests.get('https://swapi.dev/api/starships/9/', verify=False)
pprint(response.json())
