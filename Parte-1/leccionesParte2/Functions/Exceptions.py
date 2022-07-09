#Manejo de excepciones en entradas

#Ejemplo de divisón entre 0
try:
    a = input("Introduzca el numerador: ")
    b = input("Introduzca el denominador: ")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError,ValueError):
    print("Entrada no válida (letras o división entre 0)")


    

