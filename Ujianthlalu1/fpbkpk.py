angka1 = int(input('Ketik angka 1 = '))
angka2 = int(input('Ketik angka 2 = '))

i = 1
while i < max(angka1, angka2):
    if angka1 % i == 0 and angka2 % i == 0:
        x = i
    i += 1

j = angka1 * angka2
while j >= min(angka1, angka2):
    if j % angka1 == 0 and j % angka2 == 0:
        y = j
    j -= 1

print('Maka, FPB dari', angka1, 'dan', angka2, 'adalah', x)
print('Maka, KPK dari', angka1, 'dan', angka2, 'adalah', y)