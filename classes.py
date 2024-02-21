import pygame
from assets import GROUND_IMAGE, BIRD_IMAGES
from variables import scroll_speed, WIN_W, BIRD_START_POS_X, BIRD_START_POS_Y

class Ground(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = GROUND_IMAGE
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  
  def update(self):
    self.rect.x -= scroll_speed
    if self.rect.x <= -WIN_W:
      self.kill()
      
class Bird(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = BIRD_IMAGES[0]
    self.rect = self.image.get_rect()
    self.rect.center = (BIRD_START_POS_X, BIRD_START_POS_Y)
    self.image_index = 0
  
  def update(self):
    self.image_index += 1
    if (self.image_index >= 30):
      self.image_index = 0
    self.image = BIRD_IMAGES[self.image_index // 10]
    