from Vector import Vector
import imagereader
class Character:
    def __init__(self, x, y):
        self.loc = Vector(x, y)
        self.grounded = False;
        self.imagereader = imagereader.ImageReader()
        self.movingLeft = False
        self.movingRight = False

    def x(self):
        return self.loc.x;

    def y(self):
        return self.loc.y

    def tick(self):
        self.imagereader.tick()

    def setLoc(self, x, y):
        self.loc.setX(x)
        self.loc.setY(y)

    def __repr__(self):
        return self.loc.__repr__()
