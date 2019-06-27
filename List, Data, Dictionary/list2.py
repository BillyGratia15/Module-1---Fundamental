students = [
    'Andi', 
    'Budi', 
    'Caca',
    'Deni',
    'Budi'
] # bisa nulis kayak gini

newStudents = ['Ella', 'Fafa']
additionalStudents = 'Gilang'

print(students.index('Caca'))
print(students.count('Budi'))

students.extend(newStudents) #extend untuk masukin list kedalam list
print(students)

students.append(additionalStudents) #append nambahnya dipaling belakang
print(students)
print(students[-1][0])

students.insert(1, 'Zaza')
print(students)

students.remove('Budi')
print(students)

#students.pop() #delete last element
#print(students)

#students.pop(2) #delete element index ke-x
#print(students)

#students.clear() #delete all
#print(students) 

students.sort() # sort alphabetic
print(students)

students.reverse() # reverse by index
print(students)