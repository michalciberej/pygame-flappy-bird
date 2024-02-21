import pygame
from helpers import quit_game
from assets import BACKGROUND_IMAGE
from variables import WIN_W, WIN_H

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((WIN_W, WIN_H))

def main():
  while True:
    quit_game()
    
    window.fill((255,255,255))
    window.blit(BACKGROUND_IMAGE, (0,0))
    
    clock.tick(60)
    pygame.display.update()

main()