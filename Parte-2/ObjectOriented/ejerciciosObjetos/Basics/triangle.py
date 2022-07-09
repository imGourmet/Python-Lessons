
import math

class Triangle:
    def __init__(self,b,h):
        self.base = b
        self.height = h

    def area(self):
        return (self.height * self.base)/2

triangle = Triangle(3,6)

print(triangle.area())
