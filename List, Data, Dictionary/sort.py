# sorting angka

angka = [14,2,34,12,67,2]
print(angka)

jumlahkarakteryangakandisortir = 5
x = angka[0:jumlahkarakteryangakandisortir]
x.sort()
print(x)

angka[0:len(x)] = x
print(angka)