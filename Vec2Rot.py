import math


class Vec2Rot:
    def __init__(self, x=0, y=0, alpha=0):
        self.x = x
        self.y = y
        self.alpha = alpha

    def __add__(self, other):
        return Vec2Rot(self.x + other.x, self.y + other.y, self.alpha+other.alpha)

    def __sub__(self, other):
        return Vec2Rot(self.x - other.x, self.y - other.y, self.alpha-other.alpha)

    def __len__(self):
        return math.sqrt(self.x*self.x+self.y*self.y)


