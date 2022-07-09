


from cmath import pi



class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (self.radius ** 2) * pi

circle = Circle(5)

print(circle.area())


