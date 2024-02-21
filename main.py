import pygame
from helpers import quit_game
from assets import BACKGROUND_IMAGE
from variables import WIN_W, WIN_H, GROUND_POS_X, GROUND_POS_Y
from classes import *

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((WIN_W, WIN_H))

def main():
  ground = pygame.sprite.Group()
  ground.add(Ground(GROUND_POS_X, GROUND_POS_Y))
  
  while True:
    quit_game()
    
    window.fill((255,255,255))
    window.blit(BACKGROUND_IMAGE, (0,0))
    
    if len(ground) <= 2:
      ground.add(Ground(WIN_W, GROUND_POS_Y))
    
    ground.draw(window)
    
    ground.update()
    
    clock.tick(60)
    pygame.display.update()

main()