import pygame
from helpers import quit_game, spawn_pipes
from assets import BACKGROUND_IMAGE
from variables import WIN_W, WIN_H, GROUND_POS_X, GROUND_POS_Y, WHITE_COLOR, score
from classes import *

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Segoe", 52)

window = pygame.display.set_mode((WIN_W, WIN_H))

def main():
  global score

  ground = pygame.sprite.Group()
  ground.add(Ground(GROUND_POS_X, GROUND_POS_Y))
  
  bird = pygame.sprite.GroupSingle()
  bird.add(Bird())
  
  pipes = pygame.sprite.Group()
  pipes_spawn_timer = 0
  
  while True:
    quit_game()
    
    window.fill(WHITE_COLOR)
    window.blit(BACKGROUND_IMAGE, (0,0))
    
    user_input = pygame.key.get_pressed()
    
    if len(ground) <= 2:
      ground.add(Ground(WIN_W, GROUND_POS_Y))
    
    pipes.draw(window)
    ground.draw(window)
    bird.draw(window)
    
    # SCORE IS NOT DISPLAYING PROPERLY EVEN THO THE VARIABLE IS INCREMENTED --FIX
    score_text = font.render(str(score), True, pygame.Color(WHITE_COLOR))
    window.blit(score_text, (int(WIN_W / 2 - score_text.get_width() / 2), 20))
    
    if bird.sprite.alive:
      ground.update()
      bird.update(user_input)
      pipes.update()
    
    pipes_spawn_timer = spawn_pipes(pipes, pipes_spawn_timer)
    
    clock.tick(60)
    pygame.display.update()

main()