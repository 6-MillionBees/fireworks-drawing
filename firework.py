# Arden Boettcher
# 3/11/25
# Firework class

import pygame as pg
import config as c
from random import randint, choice

class Firework(pg.sprite.Sprite):
  def __init__(self, groups, pos, speed, colors):
    super().__init__(groups)
    self.pos = pos
    self.direction = pg.Vector2(0, 1).normalize()
    self.speed = speed
    self.particles = pg.sprite.Group()
    self.colors = colors
    self.main_part = particle(self.particles, self.pos, choice(colors), pg.math.Vector2(0, -1), self.speed, 1000, (10, 10))
    self.exploded = False

  def explode(self):
    self.exploded = True
    self.pos = self.main_part.pos
    self.particles.sprites()[0].kill()
    for x in range(100):
      particle(
        self.particles,
        self.pos.copy(),
        c.RED,
        c.rand_vector(),
        randint(50, 250),
        randint(500, 800)
      )

  def update(self, dt):
    self.check_speed()
    self.check_particles()
    self.particles.update(dt)

  def check_particles(self):
    if len(self.particles.sprites()) == 0:
      self.kill()

  def check_speed(self):
    if self.main_part.speed <= 0:
      if self.exploded:
        return
      self.explode()

  def draw(self, surface):
    for part in self.particles:
      part.draw(surface)


class particle(pg.sprite.Sprite):
  def __init__(self, groups, pos, color, direction, speed, falloff, size = (2, 2)) -> None:
    super().__init__(groups)
    self.pos = pos
    self.color = color
    self.direction = direction
    self.speed = speed
    self.falloff = falloff
    self.size = size
    self.lifespan = randint(100, 200)
    self.define_surf()

  def define_surf(self):
    self.image = pg.Surface(self.size).convert_alpha()
    self.image.set_colorkey(c.BLACK)

    self.rect = self.image.get_rect()

    pg.draw.rect(self.image, self.color, self.rect)


  def update(self, dt):
    self.move(dt)
    self.check_speed(dt)

  def check_speed(self, dt):
    if self.speed <= 0:
      self.speed = 0
      self.lifespan -= dt * 1000
      if self.lifespan <= 0:
        self.kill()

  def move(self, dt):
    self.pos += self.direction * self.speed * dt
    self.speed -= self.falloff * dt
    self.rect.center = self.pos

  def draw(self, surface):
    surface.blit(self.image, self.rect)