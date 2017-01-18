""" Module: 
    Show GUI window with map and robot image.
    Read and store map (pixel values)
    """

import pygame
from PIL import Image

class Map(object):
    def __init__(self, bgImPath, rbImPath):
        """ Set display size, name, clock and loads map, robot positon, array of map pixel values 
            @param bgImPath - Path to map image 
            @param rbImPath - Path to robot image
            """
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Line Follower')
        self.clock = pygame.time.Clock()
        self.carImg = pygame.image.load(rbImPath)
        self.bgImg = pygame.image.load(bgImPath)
        self.img = Image.open(bgImPath)
        self.pixels = self.img.load()


    def set_RobotPos(self, x, y, angle):
        """ Set robot image on selected position and rotate it 
            @param x - x coordinate of robot's center
            @param y - y coordinate of robot's center
            @param x - x coordinate of robot's center
            @param angle - robot's angle
            
            """
        orig_rect = self.carImg.get_rect()
        rot_image = pygame.transform.rotate(self.carImg, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()

        self.gameDisplay.blit(rot_image, (x-50,y-50))

    def map(self, x,y):
        """ Sets map image on selcted positon 
            @param x - x coordinate of left map corner
            @param y - y coordinate of left map corner
            """
        self.gameDisplay.blit(self.bgImg, (x,y))

    def print_(self):
        """ Update GUI"""
        pygame.display.update()

    def check_event(self):
        """ Check if user want to close app """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
        return "work"

    def get_PixVal(self, x, y):
        """ Return selected map's pixel value
            @param x - x coordinate of a pixel
            @param y - y coordinate of a pixel
            """
        return self.pixels[x,y]
