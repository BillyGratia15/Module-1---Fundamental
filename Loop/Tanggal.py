# time

import datetime

x = datetime.datetime.now()

# print(x)
# print(x.year)           #tahun
# print(x.strftime('%m')) #index bulan
# print(x.strftime('%B')) #bulan nama eng
# print(x.strftime('%A')) #hari eng
# print(x.strftime('%d')) #tanggal
# print(x.strftime('%H')) #jam 24h
# print(x.strftime('%I')) #jam 12h
# print(x.strftime('%M')) #menit
# print(x.strftime('%S')) #detik

# print(x.strftime('%c')) #detik
# print(x.strftime('%x'))
# print(x.strftime('%X'))

from datetime import datetime
# x = '12/12/2019'
# y = '12 Apr 2019'
# z = '12-04-19 21.45'
a = 'Friday, 12 April 2019'
# b = "Jum'at, 12 April 2019"

ubahstrkedate = datetime.strptime(a,'%A, %d %B %Y')

print(ubahstrkedate)
print(type(ubahstrkedate))
print(ubahstrkedate.strftime('%A'))


listHari = {
    'Friday': 'Jum\'at',
    'Thursday' : 'Kamis',
    'Wednesday': 'Rabu',
    'Tuesday': 'Selasa',
    'Monday' : 'Senin',
    'Sunday' : 'Minggu',
    'Saturday' : 'Sabtu'   
}

hariIni = listHari[x.strftime('%A')]
print(hariIni)

