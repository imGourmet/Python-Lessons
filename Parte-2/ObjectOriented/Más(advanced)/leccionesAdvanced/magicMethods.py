


#TODAS LAS CLASES DE PYTHON HEREDAN METODOS DE LA CLASE "Object"
#COMO ES EL EJEMPLO DE "__repr__"
#PODEMOS MODIFICAR LA SALIDA DE PRINT("CLASE")

class Lion:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name


lion = Lion("Dilbert")

print(lion)


#TAMBIÉN PODEMOS CREAR
#OPERACIONES CON LOS OBJETOS COMO OPERANDOS
#CON EL MAGIC METHOD: __add__ INTEGRADO 

class AlwaysPositive:
    def __init__(self,n):
        self.n = n

    def __add__(self,other):
        return abs(self.n + other.n)
               #|----> FUNCIÓN VALOR absOLUTO

x = AlwaysPositive(-20)
y = AlwaysPositive(10)


print(x + y)


