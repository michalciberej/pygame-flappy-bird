import random
import pygame
from classes import Pipe, Bird
from assets import TOP_PIPE_IMAGE, BOTTOM_PIPE_IMAGE


def quit_game():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()


def spawn_pipes(pipes_group, pipes_spawn_timer):
  if pipes_spawn_timer <= 0:
    x = 550
    top_y = random.randint(-700, -400)
    bottom_y = top_y + random.randint(80, 130) + BOTTOM_PIPE_IMAGE.get_height()
    pipes_group.add(Pipe(x, top_y, TOP_PIPE_IMAGE, "top"))
    pipes_group.add(Pipe(x, bottom_y, BOTTOM_PIPE_IMAGE, "bottom"))
    pipes_spawn_timer = random.randint(150, 250)
  pipes_spawn_timer -= 1
  return pipes_spawn_timer


def check_colisions(bird, pipes, ground):
    colision_pipes = pygame.sprite.spritecollide(bird.sprites()[0], pipes, False)
    colision_ground = pygame.sprite.spritecollide(bird.sprites()[0], ground, False)
    if colision_ground or colision_pipes:
      bird.sprite.alive = False