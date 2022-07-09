


class Perimeter:
    def __init__(self,side,base):
        self.side = side
        self.base = base

    def calculate_perimeter(self):
        print((self.base * 2)+(self.side*2))


class Rectangle(Perimeter):
    def __init__ (self,side,base):
        self.side = side
        self.base = base


class Square(Perimeter):
    def __init__(self,side):
        self.side = side
    def calculate_perimeter(self):
        print(self.side*4)
    




square = Square(6)       
rectangle = Rectangle(2,4)
rectangle.calculate_perimeter()
square.calculate_perimeter()


