# Arden Boettcher
# 3/11/25
# Firework class

import pygame as pg
import config as c
from random import randint, choice

class Firework(pg.sprite.Sprite):
  def __init__(self, groups, pos, height, speed):
    super().__init__(groups)
    self.pos = pos
    self.tar_pos = height
    self.speed = speed
    self.falloff = 50
    self.particles = pg.sprite.Group()
    particle(self.particles, self.pos, pg.math.Vector2(0, -1), self.speed, 50)

  def explode(self):
    self.particles.sprites()[0].kill()
    for x in range(100):
      particle(self.particles, self.pos, choice(c.RED, c.YELLOW))

  def update(self, dt):
    self.pos[1] -= self.speed
    self.speed -= self.falloff
    self.particles.update(dt)

  def draw(self, surface):
    for part in self.particles:
      part.draw(surface)


class particle(pg.sprite.Sprite):
  def __init__(self, groups, pos, color, direction, speed, falloff) -> None:
    super().__init__(groups)
    self.pos = pos
    self.color = color
    self.direction = direction
    self.speed = speed
    self.falloff = falloff

  def define_surf(self):
    self.image = pg.Surface((2, 2))
    self.image.convert_alpha()
    pg.draw.rect(self.image, )


  def update(self, dt):
    self.pos += self.direction * self.speed * dt
    self.speed -= self.falloff