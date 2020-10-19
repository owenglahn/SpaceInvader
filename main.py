# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:07:49 2020

@author: Owen
"""
import pygame

pygame.init()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800, 600))

#pygame.display.set_caption("Space Invaders!")

# this causes crash
ship = pygame.image.load("spaceship.png")
pygame.display.set_icon(ship)

#main loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            break

    screen.fill(RED)
    pygame.display.update()
    