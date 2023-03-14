# Все Изыскания здесь бесполезны. Просто создала новую учетку


# Используемые библтотеки
import requests

# Сообщение из котика о создании тренера
# Тренер успешно создан!
# {'id': '3404', 'trainer_name': 'Welz', 'trainer_token': '89fd06623c85be336b727c544d91791f'}

# Переменные
token = '89fd06623c85be336b727c544d91791f'
trainer_id = 3404

# Убить лишних покемонов POST /pokemons/kill
# !!! Убийство не освобождает слот для нового покемона
response_kill = requests.post('https://pokemonbattle.me:9104/pokemons/kill',
 headers={'Content-Type':'application/json','trainer_token':token}, json={
    "pokemon_id": 6207
})
print(response_kill.status_code)

# Удалить лтшних покемонов PUT /trainers/delete_pokeball
response_delete = requests.put('https://pokemonbattle.me:9104/trainers/delete_pokeball',
 headers={'Content-Type':'application/json','trainer_token':token}, json={
    "pokemon_id": 6211
})
print(response_delete.status_code)

#Запрос за информацией о покемонах GET /pokemons
#Можно фильтровать по квери параметрам, например по `trainer_id`, `status`, `in_pokeball`
response_info = requests.get(f'https://pokemonbattle.me:9104/pokemons?trainer_id={trainer_id}',
 headers={'Content-Type':'application/json','trainer_token':token})
print(response_info.json())

