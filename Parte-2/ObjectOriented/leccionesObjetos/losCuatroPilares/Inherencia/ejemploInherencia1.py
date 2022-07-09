


#LAS CLASES PUEDEN HEREDAR LOS ATRIBUTOS DE OTRAS CLASES
#LO QUE NOS HACE DIFERENCIAR ENTRE CLASES MADRES/HIJAS:


class Shape:
    def __init__ (self,w,l):
        self.width = w
        self.lenght = l

    def print_size(self):
        print("""{} by {}""".format(self.width,self.lenght))

my_shape = Shape(20,25)
my_shape.print_size()

#PODEMOS DEFINIR UNA CLASE HIJA
#PASÁNDOLE EL NOMBRE DE 
#LA CLASE MADRE COMO UN PARÁMETRO  :

class Square(Shape):
    pass  #--> Simplemente dice a python de no hacer nada

a_square = Square(24,89)
a_square.print_size()


