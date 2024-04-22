from Integral import Integral


def clamp(x, x_min, x_max):
    return max(min(x_max, x), x_min)


class PRegulator:

    def __init__(self, kp, U_max, U_min):
        self.kp = kp
        self.ki = ki
        self.U_max = U_max
        self.U_min = U_min

    def __call__(self, error):
        u = self.kp * error
        return clamp(u, self.U_max, self.U_min)


class IRegulator:
    def __init__(self, ki, u_min, u_max, integral: Integral):
        self.ki = ki
        self.U_max = u_max
        self.U_min = u_min
        self.integral = integral
        self.lastValue = 0

    def __call__(self, error):
        self.integral.update(error)
        u = self.integral.value * self.ki
        self.lastValue = u
        return clamp(u, self.U_max, self.U_min)


class PIRegulator:
    def __init__(self, kp, ki, u_min, u_max, integral: Integral):
        self.p = PRegulator(kp, u_min, u_max)
        self.i = IRegulator(ki, u_min, u_max, integral)

    def __call__(self, error):
        u = self.i(error)+self.p(error)
        self.lastValue = u
        return clamp(u, self.p.U_min, self.p.U_max)
