


class Horse():
    def __init__(self,color,name,owner):
        self.color = color
        self.name = name
        self.owner = owner


class Rider():
    def __init__(self,name):
        self.name = name



carlos = Rider("Carlos Gutiérrez")
horse1 = Horse("Brown","Henry",carlos)

print(horse1.owner.name)
        