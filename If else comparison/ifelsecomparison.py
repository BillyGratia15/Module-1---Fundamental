# comparison

a = 12
b = 13
c = '12'

print(a <= b)
print(a <= int(c))

nilai = 59

if nilai >= 80:
    print('Nilai anda =', nilai, '=> Anda lulus!')
elif 60 <= nilai < 80:
    print('Nilai anda =', nilai, '=> Anda remedial!')
else: 
    print('Nilai anda=', nilai, '=> Anda tidak lulus')

angka = input('Masukkan angka: ')

if angka.isdigit():
    if int(angka) % 2 == 0:
        print('Angka', angka, '=> GENAP')
    else:
        print('Angka', angka, '=> GANJIL')
else:
    print('Maaf input tidak valid')

