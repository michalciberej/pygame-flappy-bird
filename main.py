import pygame
from helpers import quit_game, spawn_pipes, check_colisions, place_in_middle
from assets import BACKGROUND_IMAGE, GAMEOVER_IMAGE, GAMESTART_IMAGE
from variables import WIN_W, WIN_H, GROUND_POS_X, GROUND_POS_Y, WHITE_COLOR
from classes import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Segoe", 52)

window = pygame.display.set_mode((WIN_W, WIN_H))
uri = "mongodb+srv://test:test@cluster0.rhab7di.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi("1"))

try:
  client.admin.command("ping")
  print(client.list_database_names)
except Exception as e:
  print(e)

game_paused = True

def main():
  global game_paused

  ground = pygame.sprite.Group()
  ground.add(Ground(GROUND_POS_X, GROUND_POS_Y))
  
  bird = pygame.sprite.GroupSingle()
  bird.add(Bird())
  
  pipes = pygame.sprite.Group()
  pipes_spawn_timer = 0
  
  coins = pygame.sprite.Group()
  
  while not game_paused:
    quit_game()
    
    passed = False
    
    window.fill(WHITE_COLOR)
    window.blit(BACKGROUND_IMAGE, (0,0))
    
    user_input = pygame.key.get_pressed()
    
    if len(ground) <= 2:
      ground.add(Ground(WIN_W, GROUND_POS_Y))
    
    pipes.draw(window)
    ground.draw(window)
    bird.draw(window)
    coins.draw(window)
    
    check_colisions(bird, pipes, ground, coins)
    
    if bird.sprite.alive:
      passed = False
      for pipe in pipes:
        passed = pipe.count()
        if passed:
          bird.sprite.score += 1
      coins.update()
      ground.update()
      pipes.update()
    else:
      window.blit(GAMEOVER_IMAGE, place_in_middle(GAMEOVER_IMAGE) )
      if user_input[pygame.K_r]:
        bird.sprite.coins = 0
        bird.sprite.score = 0
        main()
        break
    bird.update(user_input)
    
    score_text = font.render(f"Score: {str(bird.sprite.score)}", True, pygame.Color(WHITE_COLOR))
    window.blit(score_text, (int(WIN_W // 2 - score_text.get_width() // 2), 20))
    
    coin_text = font.render(f"Coins: {bird.sprite.coins}", True, pygame.Color(WHITE_COLOR))
    window.blit(coin_text, (int(WIN_W // 2 - score_text.get_width() // 2), 60))
    
    pipes_spawn_timer = spawn_pipes(pipes, pipes_spawn_timer, coins)
    
    clock.tick(60)
    pygame.display.update()


def menu():
  global game_paused
  
  while game_paused:
    quit_game()
    
    window.fill(WHITE_COLOR)
    window.blit(BACKGROUND_IMAGE, (0,0))
    window.blit(GROUND_IMAGE, (GROUND_POS_X, GROUND_POS_Y))
    window.blit(BIRD_IMAGES[0], (BIRD_START_POS_X, BIRD_START_POS_Y))
    window.blit(GAMESTART_IMAGE, place_in_middle(GAMEOVER_IMAGE))
    
    user_input = pygame.key.get_pressed()
    
    if user_input[pygame.K_SPACE]:
      game_paused = False
      main()
    
    pygame.display.update()


menu()