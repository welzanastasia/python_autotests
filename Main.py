# Используемые библтотеки
import requests

# Сообщение из котика о создании тренера
# Тренер успешно создан!
# {'id': '3407', 'trainer_name': 'Пушистая бабочка', 'trainer_token': '2539cbccdf30d4e8ae1c272d0a3dbd97'}
# Почта caj84435@nezid.com 
# Пароль Sasasa1

# Переменные
token = '2539cbccdf30d4e8ae1c272d0a3dbd97'
trainer_id = 3407

# Запрос на создание покемона POST /pokemons
response = requests.post('https://pokemonbattle.me:9104/pokemons',
 headers={'Content-Type':'application/json','trainer_token':token}, json={
    "name": "Kisa",
    "photo": "https://dolnikov.ru/pokemons/albums/1008.png"
})
print(response.json())


# Запрос на смену имени покемона PUT /pokemons 
pokemon_id = response.json()['id']
response_rename = requests.put('https://pokemonbattle.me:9104/pokemons',
 headers={'Content-Type':'application/json','trainer_token':token}, json={
    "pokemon_id": pokemon_id,
    "name": "Киса",
    "photo": ""
})
print(response_rename.json())

# Запрос на ловлю покемона в покебол POST /trainers/add_pokeball
response_add_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball',
 headers={'Content-Type':'application/json','trainer_token':token}, json={
    "pokemon_id": pokemon_id
})
print(response_add_pokeball.json())

#Запрос за информацией о покемонах GET /pokemons
#Можно фильтровать по квери параметрам, например по `trainer_id`, `status`, `in_pokeball`
response_info = requests.get(f'https://pokemonbattle.me:9104/pokemons?trainer_id={trainer_id}',
 headers={'Content-Type':'application/json','trainer_token':token})
print(response_info.json())









