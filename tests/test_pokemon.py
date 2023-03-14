# Используемые библтотеки
import requests
import pytest


# Переменные
token = '2539cbccdf30d4e8ae1c272d0a3dbd97'
trainer_id = '3407'

# Проверь, что ответ запрос GET /trainers приходит с кодом 200
def test_status_code():
    response = requests.get('https://pokemonbattle.me:9104/trainers', 
    headers={'Content-Type':'application/json'})
    assert response.status_code == 200

# Проверь, что в ответе приходит строчка с именем твоего тренера
def test_trainer_is_here():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={ 'trainer_id': trainer_id})
    assert response.json()['trainer_name'] == 'Пушистая бабочка'
