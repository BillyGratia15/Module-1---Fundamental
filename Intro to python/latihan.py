# penghitung jumlah huruf dinama seseorang (spasi tidak dihitung)
# penghitung jumlah huruf tertentu dalam suatu kata

nama = 'Billy Gratia Arya Putera'
total = len(nama)
jumlahspasi = len(nama.split(' ')) - 1
totaltanpaspasi = total - jumlahspasi


print ('Nama ' + nama + ' mengandung : ' + str(totaltanpaspasi) + ' huruf')

# ==========================================================================

# cari jumlah karakter tertentu dalam suatu nama

nama = 'Billy Gratia'
cari = 'i'
namatanpacari = nama.replace(cari, '')
jumlahcari = len(nama) - len(namatanpacari)

print(nama.split(cari))
print(nama)
print(namatanpacari)

print(len(nama) - len(namatanpacari))

print('Jumlah', cari, 'dalam', nama, 'adalah:', jumlahcari)

nama2 = 'Inneke Indriyani'
cari2 = 'i'
namatanpacari2 = nama2.replace(cari2,'')
jumlahcari2 = len(nama2) - len(namatanpacari2)

print('Jumlah', cari2, 'dalam', nama2, 'adalah: ', jumlahcari2)

kalimat = 'Billy tidak masuk Sekolah hari ini karena Sekolah kebanjiran'
cari3 = 'sekolah'

kalimattanpacari = kalimat.lower().replace(cari3.lower(),'')
selisihkarakter = len(kalimat) - len(kalimattanpacari)
jumlahcari3 = int(selisihkarakter / len(cari3))

print(kalimat)
print(len(kalimat))
print(kalimattanpacari)
print(len(kalimattanpacari))
print(selisihkarakter)
print(jumlahcari3)










