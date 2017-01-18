#!/usr/bin/python

import math

class Robot:
    def __init__(self, xpos, ypos, angle, v):
        self.xpos = xpos
        self.ypos = ypos
        self.angle = angle
        self.v = v
    def get_sensor_position(self, is_right):
        t = 10
        if is_right:
            tmp_angle = ((self.angle + 45) % 360)*3.14/180
        else:
            tmp_angle = ((self.angle - 45) % 360)*3.14/180
        return [self.xpos + t*math.sin(tmp_angle), self.ypos + t*math.cos(tmp_angle)]
    def move(self):
        tmp_angle = self.angle*3.14/180
        self.xpos += self.v*math.sin(tmp_angle)
        self.ypos += self.v*math.cos(tmp_angle)

    def change_angle(self, angle):
        self.angle = (self.angle + angle) % 360


def average(l):
    return sum(l)/float(len(l))
