"""
Тест АПИ
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '15f54aa75dfe6b7de716bf1ce8352906'}

body = {
    "name": "Krooot"
}

body2 = {
    "pokemon_id": "20794",
    "name": "Krit"
}

body3 = {
    "pokemon_id": "20794",
}


response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

response = requests.put(url=f'{URL}/pokemons', json= body2, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

response = requests.post(url=f'{URL}/trainers/add_pokeball', json= body3, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')


