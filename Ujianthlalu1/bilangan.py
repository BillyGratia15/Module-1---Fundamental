print()

bil = input("Ketik angka anda: ")

kategoriBil = []

def kategori():
    if len(bil.split('.')) > 1:       
        print('Masukkan bilangan bulat!')
    else:
        if bil.replace('-', '').isdigit() == False:
            print('Masukkan bilangan yang benar!')
        else:
            bilInput= int(bil)
            kategoriBil.append('bulat')
            if bilInput < 0:
                kategoriBil.append('negatif')
                print(kategoriBil)
            else:
                kategoriBil.append('cacah')
                if bilInput == 0:
                    return kategoriBil.append('nol')
                else:
                    kategoriBil.append('asli')
                    if bilInput % 2 == 0:
                        kategoriBil.append('genap')
                    elif bilInput%2 != 0:
                        kategoriBil.append('ganjil')
                    if bilInput > 1:
                        for i in range(2,bilInput):
                            if (bilInput % i) == 0:
                                kategoriBil.append('komposit')
                                break
                        else:
                            return kategoriBil.append('prima')
                    else:
                        return kategoriBil.append('komposit')
                    
    
kategori()
print(kategoriBil)
print()