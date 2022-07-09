


from curses.textpad import rectangle


class Shape:
    def __init__(self) -> None:
        pass
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__ (self,side,base):
        self.side = side
        self.base = base


class Square(Shape):
    def __init__(self,side):
        self.side = side


square = Square(6)
rectang = Rectangle(5,7)


rectang.what_am_i()
square.what_am_i()
    
        
