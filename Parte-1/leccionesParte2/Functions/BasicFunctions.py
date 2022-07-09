#Ejemplos de funciones 

#Con un parámetro:
def f(x):
    return x+1


z = f(4)


if z == 5:
    print("Z is 5")
else:
    print("Z is not 5")


#Sin parámetro:
def g():
    return 1+1

result0 = g()
print(result0)

#Más de un parámetro:
def p(x,y,z):
    return x + y + z 


result1 = p(1,2,3)
print(result1)


#Ejemplos de funciones integradas en Python:

print(len("longitud de caracteres"))

print(str(436)) #Conversión a string

print(int(3.4)) #Conversión a entero

print(float(10))#Conversión a decimal



