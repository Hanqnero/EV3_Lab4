class Integral:

    def __init__(self, dt, initial_value, x0):
        self.dt = dt
        self.value = initial_value
        self.x0 = x0

    def update(self, x1):
        self.value += (self.x0+x1) / 2 * self.dt
        self.x0 = x1

    def values(self):
        return self.value

