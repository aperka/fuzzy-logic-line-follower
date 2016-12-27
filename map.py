import pygame
from PIL import Image

class Map(object):
    def __init__(self, bgImPath, rbImPath):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Line Follower')
        self.clock = pygame.time.Clock()
        self.carImg = pygame.image.load(rbImPath)
        self.bgImg = pygame.image.load(bgImPath)
        self.img = Image.open(bgImPath)
        self.pixels = self.img.load()


    def set_RobotPos(self, x, y, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = self.carImg.get_rect()
        rot_image = pygame.transform.rotate(self.carImg, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()

        self.gameDisplay.blit(rot_image, (x,y))

    def map(self, x,y):
        self.gameDisplay.blit(self.bgImg, (x,y))

    def print_(self):
        pygame.display.update()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
        return "work"

    def get_PixVal(self, x, y):
        return self.pixels[x,y]




m = Map('map.png','im.png')

xpos=0
ypos=0

while m.check_event() == "work":
    print m.get_PixVal(xpos,ypos)
    m.map(0,0)
    m.set_RobotPos(xpos,ypos,ypos)
    m.print_()
    xpos=xpos+1
    ypos=ypos+1
    m.clock.tick(60)

print "exit"
