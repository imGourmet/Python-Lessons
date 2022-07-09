


class Hexagon:
    def __init__(self,s):
        self.side = s

    def perimeter(self):
        return self.side * 6

hexagon = Hexagon(97)

print(hexagon.perimeter())