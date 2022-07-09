#Loops anidados


for i in range(1,3):#---------------> #OUTER LOOP
    print(i)
    for letter in ["a","b","c"]:#---> #INNER LOOP
        print(letter)


#Ejemplo práctico con listas:

list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
    
print(added)


#FOR dentro de WHILE (y viceversa)

while input("y or n?") != 'n':
    for z in range(1,6):
        print(z)


