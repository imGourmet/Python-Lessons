#Ejemplos de variables globales y locales a una función

x = 1
y = 2
z = 3 #Estas variables son GLOBALES al estar definidas fuera y se comparten en todo el programa


def f():
    print(x)
    print(y)
    print(z)


f()


def g():     #Estas variables sin embargo solo serán utilizadas por la función en la que están definidas y no fuera 
    x = 4
    y = 5
    z = 6
    print(x)
    print(y)
    print(z)

g()  # las mismas variables pero con distinto valor no tenemos conflicto pues son explícitas a una función concreta.


#para cambiar valores de variables globales LOCALMENTE usamos "global":

def p():
    global x 
    x += 6
    print(x)

p()

