from Vector import Vector
class Character:
    def __init__(self, x, y):
        self.loc = Vector(x, y)

    def move(dx, dy):
        self.loc += Vector(dx ,dy)

    def __repr__(self):
        return self.loc.__repr__()
