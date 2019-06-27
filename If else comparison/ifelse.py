#if statement

bekerja = True
jomblo = True

if bekerja and jomblo:
    print('Anda sudah kerja, kok jomblo?')   
elif bekerja and not(jomblo):
    print('Selamat ~ ~ ~')
elif not(bekerja) and jomblo:
    print('Anda belum kerja, kok sudah taken')
else:
    print('Sana cari kerja dulu')




