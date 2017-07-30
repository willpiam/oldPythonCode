
#playing around with pygame

import pygame
import time

(width,height) = (600,400) #gives width and height values


screen = pygame.display.set_mode((width, height)) #difines window dimentions

#pygame.draw.lines(screen, color, closed, pointlist, thickness)

pygame.draw.lines(screen, (255,0,0), 1, [(0,0), (50, 100), (100, 100), (600, 400)],1)
pygame.draw.lines(screen, (0,255,0), 1, [(0,0), (55, 105), (105, 105), (605, 405)],1)
pygame.display.update() #shows the new changes i've made


i = 1#gives i value of one of infinate loop
while (i == 1):#starts infinate loop that searches for the red close butten being pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#if the red close butten is pressed the program closses
             pygame.quit(); sys.exit();
