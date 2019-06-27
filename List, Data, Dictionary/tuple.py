# [a,b,c] list = mutable
# (a,b,c) tuple = immutable
# {a,b,c} set

angkaTuple = ([1,2], 
            (7,8), 
            [3,4], 
            [5,6])

angkaList = [(1,2),
            (3,4),
            (5,6)]

print(angkaList[0][1])

angkaList[0] = 1234
print(angkaList[0])

# angkaTuple[0] = 'Andi' gagal

print(angkaTuple)
angkaTuple[1] = 'Andi'

print(angkaTuple[1])

#angkaTuple[0] = 1234 GAGAL
#print(angkaTuple[0]) ISINYA GABISA DIGANTI