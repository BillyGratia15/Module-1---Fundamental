# function

# f(x) = x + 1
import math

def tes(x,y):
    z = x ** y
    print('Hasil dari', x, '*', y, '=', x*y)
    print('Hasil dari', x, '**', y, '=', z)

tes(2, 3)    

def luasLingkaran(r):
    L = math.pi * r * r
    print('Luas lingkaran dengan r = ', r, 'adalah', L)    

luasLingkaran(7)

def luasTrapesium(a, b, t):
    LT = (a + b) * t / 2
    print('Luas trapesium dengan a =', a, 
    'b =', b, 
    't =', t, 
    'adalah', LT)

luasTrapesium(3,6,4)
