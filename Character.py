from Vector import Vector
class Character:
    def __init__(self, x, y):
        self.loc = Vector(x, y)
        self.grounded = False;

    def move(self, dx, dy):
        self.loc += Vector(dx ,dy)

    def x(self):
        return self.loc.x;

    def y(self):
        return self.loc.y

    def tick(self):
        if self.x() > 10.286 and self.x() < 10.286 + 10.786 and self.y() < 7.7:
                self.grounded = True

    def __repr__(self):
        return self.loc.__repr__()
