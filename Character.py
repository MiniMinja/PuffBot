class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return 'x: {} y: {}'.format(x, y)
