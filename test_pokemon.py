import pytest
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '15f54aa75dfe6b7de716bf1ce8352906'}

def test_get_trainers():
  """
  KTI-1. Get trainers code 200
  """
  response = requests.get(url=f'{URL}/trainers', params= {"level": 1}, headers=HEADER, timeout=5)
  assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_trainer_id():
  """
  KTI-2. Get trainers id
  """
  response = requests.get(url=f'{URL}/trainers', params= {"trainer_id": 3660}, headers=HEADER, timeout=5)
  assert response.status_code == 200, 'Unexpected status code'  