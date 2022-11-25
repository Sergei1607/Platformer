# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 18:45:08 2022

@author: serge
"""

import pygame, sys
from settings import *
from tiles import Tile
from level import Level


pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill("black")
    level.run( )
    
    
    
    pygame.display.update()
    clock.tick(60)