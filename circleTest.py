import pygame
from pygame.locals import *
import math


from Circle import Circle

pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Circle Test")

# background
background = pygame. Surface(screen. get_size ())
background = background.convert ()
background. fill ((0, 0, 30))

# x,y of the top left corner with, height
rect = (100, 100, 100, 100)
white = (255, 255, 255, 128)  # white color
red  = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)

FPS = 60


width = 3

# Main loop
running = True
t = 0
deltaT = .0125
WAVE_LENGTH = 400
wave = []
clock = pygame.time.Clock()

while running:
    # set the screen blue
    screen.blit (background, (0, 0))

    start_angle_degrees = 0 + t
    stop_angle_degrees = 350 + t
    start_angle_radians = math.radians(start_angle_degrees)
    stop_angle_radians = math.radians(stop_angle_degrees)
    t+= deltaT

    c = Circle(150,150,50)
    x,y = c.getXYCenterToRadius(start_angle_degrees)

    # updates the center of the circle, and continues
    c2 = Circle(x,y,25)
    x1,y1 = c2.getXYCenterToRadius(start_angle_degrees+t*2)

    # does the same, need to figure out how to make this recursive 
    c3 = Circle(x1,y1,25/2)    
    x2,y2 = c3.getXYCenterToRadius(start_angle_degrees+t*4)
    wave = [(x2,y2)] + wave
    # updates the display


    # first circle
    pygame.draw.line(screen, yellow, (x,y),  (c.centerX, c.centerY))
    pygame.draw.line(screen, green,  (x,y),  (x1, y1))
    pygame.draw.line(screen, yellow, (x1,y1),(x2, y2))

    # draw a line from last orbit to the start of the wave
    pygame.draw.line(screen, red, wave[0], (400,y2))
    pygame.draw.line(screen, red, wave[0], (wave[0][0],400))
    
    # draw all points in the wave
    for i in range(len(wave)):
        point = (wave[i][0],wave[i][1])
        pygame.draw.circle(screen, white, (400 + i,point[1]), 1)
        pygame.draw.circle(screen, white, (point[0],400 + i), 1)

    # draw the screen
    pygame.display.flip()

    # quit the demo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if len(wave) > WAVE_LENGTH:
        wave.pop()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
