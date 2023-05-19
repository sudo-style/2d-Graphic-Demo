import pygame
import math

from bezierToPoints import bezierToPoints # made by using ChatGPT, need to change things for it to work, and added other features
from Rainbow import get_rainbow_color

# took insparation from
# https://www.youtube.com/watch?v=MY4luNgGfms

# initialize pygame
pygame.init()

# set up the screen
width = 1920
height = 1920
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Discrete Fourier Transform")
clock = pygame.time.Clock()
FPS = 60

# colors
white = (255, 255, 255)
black = (0, 0, 30)
red = (255,0,0)

#time = 0
# Fourier Transform function
# https://en.wikipedia.org/wiki/Discrete_Fourier_transform
'''
frequency is in terms of the first rotation:
so the 4th epicycle will orbit 4 times for every 1 orbit of the first
while the 0th epicycle won't orbit at all

amplitude is the radius calculated by the magnitue of the real and imaginary cordinate
phase is the initial starting angle of the epicycle
'''
def dft(x):
    X = []
    n = len(x)
    for k in range(n): 
        re,im = 0,0
        for t in range(n):
            angle = (2*math.pi*k*t)/n
            re += x[t]*math.cos(angle)
            im -= x[t]*math.sin(angle)
        re = re/n
        im = im/n
        freq = k        
        amp = math.sqrt(re**2+im**2)
        phase = math.atan2(im,re) 
        X.append({'re':re, 'im': im, 'freq': freq, 'amp': amp, 'phase': phase})
    return X

# draw the Epicycles
'''
x,y is the starting location of the epicycle chain
The program will draw the output doesn't matter where this is placed,
but you won't see the full chain of epicycles if starting at 0,0
Both could be placed in the center of the 

fourier is the dft which has all of the information about each epicycle
rotation will depend on the axis, the x axis doesn't need a rotation, but y will be rotated 180 degrees
'''
def epicycles(x, y, fourier, rotation,time):
    for i in range(len(fourier)):
        prevx = x
        prevy = y
        freq = fourier[i]['freq']
        radius = fourier[i]['amp']  
        phase = fourier[i]['phase']
        x += radius * math.cos(freq*time+phase+rotation)
        y += radius * math.sin(freq*time+phase+rotation)
        # draws the epicycle radii 
        pygame.draw.line(screen, white, (prevx, prevy), (x, y))  
    # returns the x,y of the endpoint
    return pygame.Vector2(x, y)

def main():
    time =  0
    x,y,fourierX,fourierY = [],[],[],[]
    translate = (300,300) # this shifts the epicycles,
    
    # converts svg files curves to x,y cordinates, with a quality paramater
    drawing = bezierToPoints('Andy.svg',3)

    # extract x and y values from the drawing
    skip = 1  # if a sketch has too many points, you can skip some
    for point in drawing[::skip]:
        x.append(point[0])
        y.append(point[1])

    # perform the discrete fourier transform
    # this will figure out the starting conditions of the circle
    fourierX = dft(x)
    fourierY = dft(y)

    path = []
    while True:
        # clear the screen
        screen.fill(black)

        # draw the epicycles
        epicycles1 = epicycles(width/2, translate[1], fourierX, 0, time)

        # rotated by 180 degrees so it can do y axis movements
        epicycles2 = epicycles(translate[0], height/2, fourierY, math.pi/2, time) 
        intercection = pygame.Vector2(epicycles1.x, epicycles2.y)

        # stops appending after when finished the drawing
        if (len(path) < len(drawing)):
            path.append(intercection)

        # draws the line between the end of the last epicycle of x and y direction
        pygame.draw.line(screen,red,epicycles1,intercection,2)
        pygame.draw.line(screen,red,epicycles2,intercection,2)
        
        # draw the path
        for index, point in enumerate(path[:-1]):
            nextPoint = path[index + 1]
            colorFrequency = 5 # the smaller the faster
            color = get_rainbow_color(time/colorFrequency)
            pygame.draw.line(screen,color,point,nextPoint,5)
        
        # update time
        deltaTime = (math.pi * 2)/len(fourierY) # time needs to be in sync with the epicycles
        time += deltaTime 

        # update the display
        pygame.display.flip()
        clock.tick(FPS)

        # check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
