


class Square:
    sqrs = []

    def __init__(self,side):
        self.side = side
        self.sqrs.append((self.side))
    
    def size_print(self):
        print("""{} by {} by {} by {}.""".format(self.side,self.side,
        self.side,self.side))
        
sqr1 = Square(3)
sqr2 = Square(82)
sqr3 = Square(18)    

print(Square.sqrs)
sqr1.size_print()

