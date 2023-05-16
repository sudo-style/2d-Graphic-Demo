import pygame
import math

from Circle import Circle

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Circle Test")

# background
background = pygame. Surface(screen. get_size ())
background = background.convert ()
background. fill ((0, 0, 255))

# x,y of the top left corner with, height
rect = (100, 100, 100, 100)
color = (255, 255, 255, 128)  # white color
width = 3

# Main loop
running = True
t = 0
deltaT = .0025
WAVE_LENGTH = 400


wave = []

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

    wave = [y2] + wave
    #print(x,y)

    # updates the display
    #pygame.draw.circle(screen, color, (150,150), width)
    # first circle
    pygame.draw.line(screen, color, (x,y), (c.centerX, c.centerY))
    pygame.draw.line(screen, color, (x,y), (x1, y1))
    pygame.draw.line(screen, color, (x1,y1), (x2, y2))


    # draw all points in the wave
    for i in range(len(wave)):
        point = wave[i]
        pygame.draw.circle(screen, color, (200 + i,point), 1)

    # draw the screen
    pygame.display.flip()

    # quit the demo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if len(wave) > WAVE_LENGTH:
        wave.pop()
pygame.quit()
