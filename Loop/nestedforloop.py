#nested for loop

listku = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]

for baris in listku:
    for elemen in baris:
        print(elemen)

data = [
    [
        ['Andi', 'Budi', 'Caca'],
        ['Deni', 'Ella', 'Fafa'],
        ['Gigi', 'Hani', 'Inne']
    ],
    [
        ['Jaja', 'Kaka', 'Lala'],
        ['Mama', 'Nana', 'Opik'],
        ['Papa', 'Qiqi', 'Riri']
    ]
]

for i in data:
    for j in i:
        for k in j:
            print(k)
