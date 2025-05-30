import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7afcd330135ee444af0b11f9ac4396ae'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '33488'

def test_status_code():
   response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
   assert response.status_code == 200

def test_trainer_name():
   response_get = requests.get(url = f'{URL}/me', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
   assert response_get.json()["data"][0]['trainer_name'] == 'Grand master byte'