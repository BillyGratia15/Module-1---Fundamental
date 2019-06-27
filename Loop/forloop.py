# looping#2
# for loop

# kata = 'Andianto'
# for huruf in kata:
#     print(huruf)

angka = [11, 22, 33, 44, 55, 66]
for x in angka:
    print(x)

# for i in range(len(angka)):
#     print(angka[i])

star = ''
for i in range(5):
    star += '* '
    print(star)

for i in reversed(range(5)):
    for j in range(i+1):
        print('* ', end='')
    print()

# angka = ''
# for i in range(5):
#     angka += str(i) + ' '
#     print(angka)


# for i in range(5):
#     for j in range(5):
#         print(i, 'dan', j)


