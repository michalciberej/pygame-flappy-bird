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
  
  bird = pygame.sprite.GroupSingle()
  bird.add(Bird())
  
  while True:
    quit_game()
    
    window.fill((255,255,255))
    window.blit(BACKGROUND_IMAGE, (0,0))
    
    user_input = pygame.key.get_pressed()
    
    if len(ground) <= 2:
      ground.add(Ground(WIN_W, GROUND_POS_Y))
    
    ground.draw(window)
    bird.draw(window)
        
    if bird.sprite.alive:
      ground.update()
      bird.update(user_input)
    
    clock.tick(60)
    pygame.display.update()

main()