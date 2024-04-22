from ev3dev2.motor import LargeMotor
from Vec2Rot import Vec2Rot
from Regulator import PIRegulator


class Robot:
    def __init__(self, left_motor: LargeMotor, right_motor: LargeMotor, linear_reg: PIRegulator,
                 angular_reg: PIRegulator):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.linear_regulator = linear_reg
        self.angular_regulator = angular_reg

    def goto(self, target: Vec2Rot):

