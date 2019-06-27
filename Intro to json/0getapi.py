
# GET API https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=Arsenal

import requests
import json

namaKlub = input('Masukkan Nama Klub : ')

url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+namaKlub

players = requests.get(url)

# print(players.json())

for player in players.json()['player']:
    print(player['strPlayer'], '(', player['strNationality'],')')





