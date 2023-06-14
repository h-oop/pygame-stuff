#pygame wooooooo

import pygame
from pygame.locals import *

#initialising pygame

#defining size of game window



#event loops? help react to events, interact w user
#this loop prints all events to console
#while True:
#    for event in pygame.event.get():
#        print(event)

#colours!
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#now I can do this to my screen
running = True
background = GRAY
key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

print(key_dict)


pygame.init()
screen = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("This Is Window Captioonnnnn")


while running:
    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

        #event listener type beat
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]

                pygame.display.set_caption(f"background colour = {background}")

    screen.fill(background)
    pygame.display.flip()


#quit pygame
pygame.quit()