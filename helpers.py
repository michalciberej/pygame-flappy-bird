import random
import pygame
from classes import Pipe, Coin
from assets import TOP_PIPE_IMAGE, BOTTOM_PIPE_IMAGE
from variables import WIN_H, WIN_W, COIN_SIZE


def quit_game():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()


def spawn_pipes(pipes_group, pipes_spawn_timer, coins):
  if pipes_spawn_timer <= 0:
    x = 550
    gap = random.randint(80, 130)
    top_y = random.randint(-700, -400)
    bottom_y = top_y + gap + BOTTOM_PIPE_IMAGE.get_height()
    pipes_group.add(Pipe(x, top_y, TOP_PIPE_IMAGE, "top"))
    pipes_group.add(Pipe(x, bottom_y, BOTTOM_PIPE_IMAGE, "bottom"))
    coins.add(Coin((x + (TOP_PIPE_IMAGE.get_width() // 2)) - COIN_SIZE[0] // 2, top_y + TOP_PIPE_IMAGE.get_height() + gap // 2 - COIN_SIZE[1] // 2 ))
    pipes_spawn_timer = random.randint(150, 250)
  pipes_spawn_timer -= 1
  return pipes_spawn_timer


def check_colisions(bird, pipes, ground, coins):
    colision_pipes = pygame.sprite.spritecollide(bird.sprites()[0], pipes, False)
    colision_ground = pygame.sprite.spritecollide(bird.sprites()[0], ground, False)
    colision_coin = pygame.sprite.spritecollide(bird.sprites()[0], coins, False)
    if colision_ground or colision_pipes:
      bird.sprite.alive = False
    if colision_coin:
      coins.sprites()[0].kill()
      bird.sprite.coins += 1


def place_in_middle(image):
  return ((WIN_W / 2 - image.get_width() / 2), (WIN_H / 2 - image.get_height() / 2))