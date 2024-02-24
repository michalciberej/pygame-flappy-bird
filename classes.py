import pygame
from assets import GROUND_IMAGE, BIRD_IMAGES, COIN_IMAGES
from variables import WIN_W, BIRD_START_POS_X, BIRD_START_POS_Y, BOTTOM_BORDER, TOP_BORDER, COIN_SIZE, SCROLL_SPEED

class Ground(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = GROUND_IMAGE
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  
  def update(self):
    self.rect.x -= SCROLL_SPEED
    if self.rect.x <= -WIN_W:
      self.kill()


class Bird(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = BIRD_IMAGES[0]
    self.rect = self.image.get_rect()
    self.rect.center = (BIRD_START_POS_X, BIRD_START_POS_Y)
    self.image_index = 0
    self.velocity = 0
    self.fly = False
    self.alive = True
    self.coins = 0
    self.score = 0
    self.immunity = False

  def update(self, user_input):
    self.image_index += 1
    if (self.image_index >= 30):
      self.image_index = 0
    self.image = BIRD_IMAGES[self.image_index // 10]

    self.velocity += 0.5
    
    if self.velocity > 6:
      self.velocity = 6
    if self.rect.y < BOTTOM_BORDER:
      self.rect.y += int(self.velocity)
    if self.rect.y >= BOTTOM_BORDER:
      self.alive = False
    if self.velocity == 0:
      self.fly = False
    if not self.alive and not self.immunity:
      self.image = BIRD_IMAGES[0]
    
    if user_input[pygame.K_SPACE] and self.rect.y > TOP_BORDER and not self.fly and self.alive:
      self.fly = True
      self.velocity = -6
    
    self.image = pygame.transform.rotate(self.image, self.velocity * -6)



class Pipe(pygame.sprite.Sprite):
  def __init__(self, x, y, image, type):
    pygame.sprite.Sprite.__init__(self)
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.type = type
    self.entered = False
    self.exited = False
    self.passed = False
    self.counted = False

  def update(self):
    self.rect.x -= SCROLL_SPEED
    if self.rect.x <= -WIN_W:
      self.kill()

    if self.type == "bottom":
      if BIRD_START_POS_X > self.rect.topleft[0] and not self.passed:
        self.entered = True
      if BIRD_START_POS_X > self.rect.topright[0] and not self.passed:
        self.exited = True
      if self.entered and self.exited and not self.passed:
        self.passed = True
    
  def count(self):
    if not self.counted and self.passed and self.type == "bottom":
      self.counted = True
      return self.counted
  


class Coin(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.smoothscale(COIN_IMAGES[0], COIN_SIZE)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.image_index = 0
  
  def update(self):
    self.image_index += 1
    
    self.rect.x -= SCROLL_SPEED
    if self.rect.x <= -WIN_W:
      self.kill()
    
    if (self.image_index >= 50):
      self.image_index = 0
    self.image = pygame.transform.smoothscale(COIN_IMAGES[self.image_index // 10], COIN_SIZE)