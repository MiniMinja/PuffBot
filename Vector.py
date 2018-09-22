class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        if isinstance(other, (int, long, float, double)):
            self.x *= other
            self.y *= other
            return other
        else:
            raise ValueError('You tried to multiply this vector with a non-number')

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
        
    def __repr__(self):
        return 'x: {} y: {}'.format(x, y)
