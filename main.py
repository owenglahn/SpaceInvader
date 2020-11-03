# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:07:49 2020

@author: Owen
"""
import pygame

pygame.init()

# color constants
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 20)

screen = pygame.display.set_mode((800, 600)) # initialize screen
pygame.display.set_caption("Space Invaders!") # set caption

#load spaceship icon
ship = pygame.image.load("spaceship.png")
pygame.display.set_icon(ship)

# game loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # window closed
            RUNNING = False # end the game loop
            break

    screen.fill(DARK_BLUE) # make screen dark blue
    pygame.display.update() # updates any changes to the pygame surface
    