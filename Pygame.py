
#pygame program to move a ball around a box based on keyboard input
#start date: febuary 9th 2016
#William Doyle
#Google will be used

import pygame
import time

(width,height) = (600,400) #gives width and height values


screen = pygame.display.set_mode((width, height)) #difines window dimentions

#pygame.draw.lines(screen, color, closed, pointlist, thickness)

pygame.draw.lines(screen, (255,0,0), 1, [(100,100), (150,200), (200,100)], 1)
pygame.draw.lines(screen, (255,0,0), 1, [(50,50), (50, 100), (100, 100), (100, 50)],1)#makes a box ... Mr.floyd did this line when I showed him the program
pygame.display.update() #shows the new changes i've made


i = 1#gives i value of one of infinate loop
while (i == 1):#starts infinate loop that searches for the red close butten being pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#if the red close butten is pressed the program closses
             pygame.quit(); sys.exit();
