data = {'Andi', 'Budi', 'Caca'}

#for elemen in data:
#    print(elemen) #harus di tab

data.add('Deni') #cuma bisa 1 elemen
data.update(['Eka','Fafa']) #bisa lebih dari 1 elemen. Dalemnya mau pake list tuple or set terserah

print(data)


#data.remove('Zizi') #error
#data.discard('Zizi') #ga ngaruh apa2 tp tetep jalan

data.clear()
print(data)

