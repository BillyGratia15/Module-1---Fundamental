# variables

nama = 'Billy Gratia Arya Putera'
usia = 23 
v = 3j #complex
w = False #boolean
x = 7500 #integer
y = 12.34 #string

print('Hai ' + 'nama ' + 'saya ' + (nama))
print('Saya ' + 'berusia ' + str(usia) + ' tahun')

print(type(v))
print(type(w))
print(type(x))
print(type(y))

print(nama.lower())
print(nama.upper())
print(nama.islower())
print(nama.isupper())

print(nama.lower().islower())
print(nama.upper().isupper())
print(type(nama.upper().isupper()))

print(len(nama))
print(len(nama) - 1)
print(nama[0])
print(nama[len(nama) - 1])

print(nama.index('G'))
print(nama.index('Gratia'))

print(nama.replace('Gratia', 'Grates'))

print(nama.split(' '))
print(nama.split(' ')[1])

