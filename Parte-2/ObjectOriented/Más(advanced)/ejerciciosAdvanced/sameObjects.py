


class Nums:
    def __init__(self,n):
        self.n = n

    def __add__(self,other):
        if self.n is other.n:
            return True
        else:
            return False

x = Nums(3)
y = Nums(3)
print(x + y) ("hola")
            
