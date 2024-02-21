import pygame
from assets import GROUND_IMAGE, BIRD_IMAGES
from variables import scroll_speed, WIN_W, BIRD_START_POS_X, BIRD_START_POS_Y, BOTTOM_BORDER, TOP_BORDER, score

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
    self.velocity = 0
    self.fly = False
    self.alive = True

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
    
    if user_input[pygame.K_SPACE] and self.rect.y > TOP_BORDER and not self.fly:
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

  def update(self):
    global score

    self.rect.x -= scroll_speed
    if self.rect.x <= -WIN_W:
      self.kill()

    if self.type == "bottom":
      if BIRD_START_POS_X > self.rect.topleft[0] and not self.passed:
        self.entered = True
        print("entered " + str(self.entered))
      if BIRD_START_POS_X > self.rect.topright[0] and not self.passed:
        self.exited = True
        print("exited " + str(self.exited))
      if self.entered and self.exited and not self.passed:
        self.passed = True
        print("passed " + str(self.passed))
        score += 1
        print(score)