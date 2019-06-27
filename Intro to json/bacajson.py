# import json

# convert dict => json

# x = {
#     'nama' : 'Andi',
#     'usia' : 23
# }

# x2 = ['Andi', 'Budi']

# y = json.dumps(x)
# y2 = json.dumps(x2)

# z1 = 'Aku Andi'
# z2 = json.dumps(z1)

# print(x)
# print(y)
# print(x2)
# print(y2)
# print(z2)

# ubah json => python

import json
x = '{"nama" : "Andi"}'
x2 = '["Andi", "Budi", "Caca"]'

y = json.loads (x)
y2 = json.loads (x2)

print(x)
print(y)
print(y['nama'])
print(x2)
print(y2)
print(y2[1])


