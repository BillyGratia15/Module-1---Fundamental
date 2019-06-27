
import json
x = {
    'id' : 2,
    'kota': 'Medan'
}

x2 = json.dumps(x)

jsonku = open('medan.json', 'w')
jsonku.write(x2)