'''
Andi & Budi
total usia Andi & Budi = 49
rasio usia Andi / Budi = 0.4

andi + budi = 49
andi / budi = 0.4 => andi = 0.4 * budi

(0.4 * budi) + (1*budi) = 49
1.4 * budi = 49
budi = 49 / 1.4 = 35
andi = 49 - 35 


andi?
budi?
'''

total = int(input('Total usia = '))
rasio = float(input('Rasio usia = '))

andi = int(total / (1+rasio))
budi = int(total - andi)

print('Usia andi = ', andi, 'th & usia budi =', budi, 'th')

