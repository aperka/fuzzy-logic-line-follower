#!/usr/bin/python
import sys
from app.map.map import Map
from app.fuzzy_logic.model import Model
from app.robot.robot import Robot


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if len(sys.argv) > 1:
    map_number = sys.argv[1]


    if map_number == '2':
        xpos = 230
        ypos = 280
        angle = 90
        v = 1
    
        m = Map('app/images/map2.png','app/images/im.png')
        robot = Robot(xpos, ypos, angle, v)
        model = Model()
    elif map_number == '1':
        xpos = 120
        ypos = 380
        angle = 90
        v = 1
        
        m = Map('app/images/map1.png','app/images/im.png')
        robot = Robot(xpos, ypos, angle, v)
        model = Model()
    else:
        print 'run.py 1 \r\n or \r\nrun.py 2'
        sys.exit()


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

    m.clock.tick(100)
print "exit"
