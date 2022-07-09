


#LOS NUEVOS MÉTODOS DEFINIDOS EN LAS
#CLASES HIJAS NO AFECTAN A LAS CLASES MADRES
#-------------------------------------------#

class Shape:
    def __init__ (self,w,l):
        self.width = w
        self.lenght = l

    def print_size(self):
        print("""{} by {}""".format(self.width,self.lenght))


class Square(Shape):
    def area(self):
        return self.width * self.lenght
#-------------------------------------------#

    #PODEMOS SOBREESCRIBIR LOS MÉTODOS HEREDADOS SIN AFECTAR 
    #A SU CLASE MADRE-----> "Method Overriding"  :

    def print_size(self):
        print("""I am {} by {}
        """.format(self.width,self.lenght))

a_square = Square(24,89)
print(a_square.area())
a_square.print_size()







