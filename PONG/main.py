#PONG YIPPEE

import pygame
import os
import random
from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('poing :)')

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 5, HEIGHT)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 125
FPS = 60
VEL = 5
BALL_VEL = [6,5]


def draw_window(p_red, p_blue, ball, red_pts, blue_pts):
    WIN.fill(BLACK)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(WIN, WHITE, BORDER)

    pygame.draw.rect(WIN, RED, p_red)
    pygame.draw.rect(WIN, BLUE, p_blue)
    ball.draw(WIN)
    pygame.display.update()

def handle_collision(ball, p_red, p_blue):
    if ball.y + ball.raduis >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x < 0:
        ball.x_vel *= -1
    elif ball.x + ball.radius <= WIDTH:
        ball.x_vel *= -1


def red_handle_movement(keys_pressed, p_red):
    if keys_pressed[pygame.K_w] and p_red.y - VEL > 0 : #UP
        p_red.y -= VEL
        
    if keys_pressed[pygame.K_s] and p_red.y + p_red.height < HEIGHT - 15: #DOWN
        p_red.y += VEL

def blue_handle_movement(keys_pressed, p_blue):
    if keys_pressed[pygame.K_UP] and p_blue.y - VEL > 0 : #UP
        p_blue.y -= VEL
        
    if keys_pressed[pygame.K_DOWN] and p_blue.y + p_blue.height < HEIGHT - 15: #DOWN
        p_blue.y += VEL

class Ball:
    MAX_VEL = 7

    def __init__(self,x,y,radius):

        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel


def main():
    p_red = pygame.Rect(10, 300, PADDLE_WIDTH, PADDLE_HEIGHT)
    p_blue = pygame.Rect(WIDTH-PADDLE_WIDTH-10, 300 , PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH // 2, HEIGHT // 2, 7)

    red_pts = 0
    blue_pts = 0

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        ball.move()
        #
        #if ball.left < 0 or ball.right > WIDTH or p_red.colliderect(ball) or p_blue.colliderect#(ball):
        #    BALL_VEL[1] += random.uniform(-1, 1)
        #    BALL_VEL[0] = -BALL_VEL[0]

        #if ball.top < 0 or ball.bottom > HEIGHT:
        #    BALL_VEL[1] += random.randrange(-1, 1)
        #    BALL_VEL[1] = -BALL_VEL[1]


        keys_pressed = pygame.key.get_pressed()
        red_handle_movement(keys_pressed, p_red)
        blue_handle_movement(keys_pressed, p_blue)
        draw_window(p_red, p_blue, ball, red_pts, blue_pts)

    pygame.quit()


main()