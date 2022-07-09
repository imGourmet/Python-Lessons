


#EJEMPLO PRÁCTICO DE VARIABLES DE CLASE, COMPARTIDAS
#CON LOS OBJETOS DE la CLASE, QUE TIENEN SUS PROPIAS 
#VARIABLES DE INSTANCIA


class Rectangle():
    recs = [] #----------> VARIABLE DE CLASE

    def __init__(self,w,l):
        self.width = w   #----> VARIABLE DE INSTANCIA 
        self.lenght = l 
        self.recs.append((self.width,self.lenght))

    def print_size(self):
        print("""{} by {}"""
        .format(self.width,self.lenght))

r1 = Rectangle(5,8)
r2 = Rectangle(2,4)
r3 = Rectangle(6,9)

print(Rectangle.recs)


