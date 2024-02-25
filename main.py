import pygame
import socket
from data.helpers import quit_game, spawn_pipes, check_colisions, place_in_middle
from data.assets import BACKGROUND_IMAGE, GAMEOVER_IMAGE, GAMESTART_IMAGE
from data.variables import WIN_W, WIN_H, GROUND_POS_X, GROUND_POS_Y, WHITE_COLOR, ORANGE_COLOR
from data.classes import *
from pymongo import DESCENDING
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

pygame.init()
clock = pygame.time.Clock()
big_font = pygame.font.SysFont("Segoe", 52)
small_font = pygame.font.SysFont("Segoe", 32)

window = pygame.display.set_mode((WIN_W, WIN_H))
uri = "mongodb+srv://test:test@cluster0.rhab7di.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi("1"))
db = client.scores.score

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
  
  user_name = socket.gethostname()
  data_sent = False
  leaderboard = []
  player_scores = []
  
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
      if not data_sent and bird.sprite.score > 0:
        db.insert_one({"user_name": user_name, "score": bird.sprite.score})
        leaderboard = db.find().sort("score", DESCENDING).limit(10)
        data_sent = True
        
      for index, player in enumerate(leaderboard):
        index += 1
        player_text = small_font.render(f"{index}. {player['user_name']} - {player['score']}", True, pygame.Color(ORANGE_COLOR))
        player_scores.append(player_text)

      window.blit(GAMEOVER_IMAGE, place_in_middle(GAMEOVER_IMAGE) )
      if user_input[pygame.K_r]:
        main()
        break
    bird.update(user_input)
    
    y = 400
    for player in player_scores:
      window.blit(player, (WIN_W // 2 - player_text.get_width() // 2, y))
      y += 20
    
    score_text = big_font.render(f"Score: {str(bird.sprite.score)}", True, pygame.Color(WHITE_COLOR))
    window.blit(score_text, (int(WIN_W // 2 - score_text.get_width() // 2), 20))
    
    coin_text = big_font.render(f"Coins: {bird.sprite.coins}", True, pygame.Color(WHITE_COLOR))
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