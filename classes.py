import pygame
from assets import GROUND_IMAGE
from variables import scroll_speed, WIN_W

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