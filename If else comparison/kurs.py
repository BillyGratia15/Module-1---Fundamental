#konversi mata uang IDR => USD / USD=> IDR
#input('Input konversi yang diinginkan')
# input('Input nilai = ')
# print('Hasil konversi = ')

kurs = {
    '1' : 0.00071,
    '2' : 14157
}

def konversi():
    print('Selamat datang di web CurrencyConverter.com')
    print('Silakan pilih metode konversi : ')
    print('1. IDR ke USD')
    print('2. USD ke IDR')
    metode = input('Ketik pilihan anda : ')
    if metode == '1':
        if nominal.replace('.', '').replace(',', '').isdigit():
            hasil = float(nominal.replace(',', '.')) * kurs[metode]
            print('Hasil konversi = $', hasil)
        else:
            print('Mohon inputkan hanya angka')    
    elif metode == '2':
        if nominal.replace('.', '').replace(',', '').isdigit():
            hasil = float(nominal.replace(',', '.')) * kurs[metode]
            print('Hasil konversi = Rp, hasil)
        else:
            print('Mohon inputkan hanya angka')   
    else:
        nominal = input('Ketik nominal Dollar: $ ')  
        if nominal.replace('.', '').replace(',', '').isdigit():
            hasil = float(nominal.replace(',', '.')) * kurs[metode]
            print('Hasil konversi = Rp', hasil)
        else:
            print('Mohon inputkan hanya angka 1 atau 2')

konversi()
