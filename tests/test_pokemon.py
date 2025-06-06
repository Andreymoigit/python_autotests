"""
Test example
"""
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7afcd330135ee444af0b11f9ac4396ae'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '33488'

def test_status_code():
    """
    GT-1. Check status code
    """
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID},
                            timeout=5)
    assert response.status_code == 200, "Unexpected status code"

def test_trainer_name():
    """
    GT-2. Check trainer name
    """
    response_get = requests.get(url = f'{URL}/me', headers = HEADER, 
                                params = {'trainer_id' : TRAINER_ID},
                                timeout=5)
    assert response_get.json()["data"][0]['trainer_name'] == 'Grand master byte', \
        "Unexpected value for trainer_name"
