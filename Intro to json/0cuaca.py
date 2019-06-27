
import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q='

namaKota = input('Ketik nama kota : ')
apikey = 'd4c0756a57f6faeef72c765deabefb6d'

dataCuaca = requests.get(url+namaKota+'&APPID='+apikey)

cuaca = dataCuaca.json()['weather'][0]['main']
suhu = dataCuaca.json()['main']['temp']
kelembaban = dataCuaca.json()['main']['humidity']

print('Cuaca =',cuaca)
print('Suhu =', round(suhu-273,2), 'celcius')
print('Kelembaban =', kelembaban, '%')