# {'key' : 'value'} dictionary

namaHari = {
    'Monday' : 'Senin',
    'Tuesday' : 'Selasa',
    'Wednesday' : 'Rabu'
    }

print(type(namaHari))

print(namaHari.keys())
print(list(namaHari.keys()))

print(namaHari.values())
print(list(namaHari.values()))

#akses key by value
print(list(namaHari.keys())[list(namaHari.values()).index('Senin')])

print(namaHari['Monday']) #pakeini lebih singkat
#print(namaHari.get('Tuesday')) #versi python lama ini biasanya pake get

#print(namaHari.get['Friday','Maaf data tidak tersedia']) gabisa
#print(namaHari.get('Friday','Maaf data tidak tersedia')) #harus pake get kalau data tidak ada

#namaHari['Monday'] = 'Senin :D'
#namaHari['Thursday'] = 'Kamis'
#print(namaHari)

#namaHari.pop('Monday')
#print(namaHari)


