#test game?
#objective:
    #make a moveable character and playspace

import pygame
from pygame.locals import *
import random

size = 800,600
width, height = size

pygame.init()
screen = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("This Is Window Captioonnnnn")


#key_dict = {K_UP:UPKEY, K_DOWN:DOWNKEY, K_LEFT:LEFTKEY, K_RIGHT:RIGHTKEY}
WHITE = (255, 255, 255)
background = (WHITE)

posx = 400
posy = 300
ball = pygame.image.load("ball.gif")
rect = ball.get_rect()

running = True


while running:
    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

        #event listener type beat
        if event.type == KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if posx < width and posx > 0:
                    posx -= 1

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if posx < width and posx > 0:
                    posx += 1
                    
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if posy < height and posx > 0:
                    posy += 1

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if posy < height and posx > 0:
                    posy -= 1

    print (f"({posx},{posy})")
    screen.fill(background)
    pygame.display.flip()

#quit pygame
pygame.quit()