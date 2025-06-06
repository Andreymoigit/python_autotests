"""
Basic
"""
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7afcd330135ee444af0b11f9ac4396ae'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

# 1.Создать покемона
# body_create = {
#     "name": "пикачу",
#     "photo_id": 14
# }

# response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
# print(response_create.text)

# # 2.Изменить имя покемону
# body_rename = {
#     "pokemon_id": "325936",
#     "name": "Бульбазавр",
#     "photo_id": 2
# }

# response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
# print(response_rename.text)


# 3.Поймать покемона в покеболл

body_add_pokeball = {
    "pokemon_id": "325936"
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball',
                                      headers = HEADER, json = body_add_pokeball,
                                      timeout=5)
print(response_add_pokeball.text)
