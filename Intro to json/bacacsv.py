
# file = open('./bacadata.csv','r')

# print(file.read())

import csv
myData = []

with open ('bacadata.csv','r') as fileku:
    # baca = csv.reader(fileku, delimiter = ',') #kalau delimiternya koma ga harus ditulis
    # for i in baca:
    #     print(i)
    baca = csv.DictReader(fileku, delimiter = ',')
    for i in baca:
        # print(dict(i))
        myData.append(dict(i))    

print(myData)