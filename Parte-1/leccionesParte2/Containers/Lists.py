#Litados


fruit = ["Apple","Orange","Pear"]



#Añadir elementos a una lista:

fruit.append("Banana")
fruit.append("Peach")
print(fruit)


random = []
random.append("39")
random.append("Colorines")
random.append("28.98")
print(random)

print(fruit[0]) #índice de listados


#añandir elementos a listas:

fruit [3] = "Pineapple"
print(fruit)

#Eliminar elementos en una lista:

fruit.pop() #Si no se especifica elimina el último puesto de la lista
print(fruit)

#Sumar listas es posible:

print(random + fruit)

#Comprobación de elementos en una lista

print("Apple" in fruit)

#Longitud de listas:

print(len(fruit + random))


#Ejemplo de uso práctico:

guess = input("¿Qué frutas he comprado?")

if guess in fruit:
    print("¡Correcto!")
else:
    print("¡Incorrecto!")