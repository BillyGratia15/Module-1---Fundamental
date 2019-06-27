# input ('ketik password : ')
# print ('Password benar: ')
# input ('ketik password : ')
# print ('Password salah: ') kalo salah 3x
# print ('Mohon maaf akun anda kami blokir')

password = '12345'
userinput = ''
inputke = 0
batasmax = 2
melebihi = False

while userinput != password and not melebihi:
    if inputke <= batasmax:
        userinput = input('Masukkan password : ')
        if userinput != password and inputke < batasmax:
            inputke += 1
            print('Input ke-', inputke, 'Password salah! Ulangi')
        elif userinput != password and inputke == batasmax:    
            inputke += 1
            print('Password salah 3x! Kesempatan habis!')
            print('Mohon maaf anda sudah salah 3x')
            print('Coba lagi esok hari!')
        else:
            print('Login sukses!')
    else:
        # melebihi = True
        break
        # print('Mohon maaf anda sudah salah 3x')
        # print('Coba lagi esok hari')