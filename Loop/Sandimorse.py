# Sandi morse

morse = {
    'A' : '• –',
    'B' : ' – • • •',
    'C' : '– • – •',
    'D' : '– • •',
    'E' : '•',
    'F' : '• • – •',
    'G' : '– – •',
    'H' : '• • • •',
    'I' : '• •',
    'J' : '• – – –',
    'K' : '– • –',
    'L' : '• – • •',
    'M' : '– –',
    'N' : '– •',
    'O' : '– – –',
    'P' : '• – – •',
    'Q' : '– – • –',
    'R' : '• – •',
    'S' : '• • •',
    'T' : '–',
    'U' : '• • –',
    'V' : '• • • –',
    'W' : '• – –',
    'X' : '– • • –',
    'Y' : '– • – –',
    'Z' : '– – • •'
}

x = input('Masukkan nama anda : ')
y = list(x.upper())

def huruf():
    for a in range(len(y)):
        y[a] = morse[y[a]]
    z = ''
    for i in y:
        z += str(i) + '/'
    print(z)

def sandi():
    y = x.split('/')
    for a in range(len(y)):
        y[a] = list(morse.keys())[list(morse.values()).index(y[a])]
    z = ''
    for i in y:
        z += str(i)
    print(z)

if y[0] in list(morse.keys()):
    huruf()
elif y[0] == '_' or '.':
    sandi()
else:
    print('Masukkan huruf atau sandi yang benar!')   

print()


      
