# lambda function

def x(a,b,c):
    return a + b + c

y = lambda a,b,c : a + b +c

print(x(1,2,3))
print(y(4,5,6))

def kali(n):
    return lambda x : x * n

kalidua = kali (2)
kalitiga = kali (3)

# print(kalidua(22))
# print(kalitiga(33))

def y(a):
    return a
def x(a):
    print(y(a))
x(12)

def z():
    return lambda c : c
b = z()

print(b(13))