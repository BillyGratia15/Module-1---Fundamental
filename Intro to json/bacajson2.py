
import json

with open('data.json') as dataku:
    data = json.load(dataku) #load = buat file ; loads = buat string

print(data)
print(type(data))
print(data[0]['nama'])
