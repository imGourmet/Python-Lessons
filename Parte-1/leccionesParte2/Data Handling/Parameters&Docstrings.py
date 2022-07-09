#Ejemplo de parámetros opcionales:

def f(x=3):
    return x ** 3

print(f()) #Usamos el parámetro definido en el argumento de la función
print(f(5))#O le asignamos otro valor a x


#Parámetros definidos Y opcionales:

def suma(x, y=10):
    return x + y

resultado = suma(5) #asignamos el valor 5 a X pero la variable Y ya está definida con valor 10 (opcional)
print(resultado)



#Docstrings usadas para describir a devs. el tipo de dato requerido en una función:

def resta(x, y):
    """""
    Returns x - y.
    :param x: int.      
    :param y: int.
    :return: int substraction of x and y.  
    """""
    return x - y

resultado_2 = resta(7,3)
print(resultado_2)
