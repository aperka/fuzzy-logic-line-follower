#!/usr/bin/python

from map import Map
from model import Model
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

xpos = 120
ypos = 380
angle = 90
v = 1

m = Map('map1.png','im.png')
robot = Robot(xpos, ypos, angle, v)
model = Model()


while m.check_event() == "work":
    m.map(0, 0)
    m.set_RobotPos(robot.xpos, robot.ypos, robot.angle)
    m.print_()

    left_sensor_pos = robot.get_sensor_position(False)
    right_sensor_pos = robot.get_sensor_position(True)

    left_sensor_val =  m.get_PixVal(left_sensor_pos[0], left_sensor_pos[1])
    right_sensor_val =  m.get_PixVal(right_sensor_pos[0], right_sensor_pos[1])


    angle = model.get_angle(left_sensor_val, right_sensor_val)

    robot.change_angle(-angle/10)
    robot.move()

    m.clock.tick(60)
print "exit"
