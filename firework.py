# Arden Boettcher
# 3/11/25
# Firework class

import pygame as pg
import config as c
from random import randint, choice

class Firework(pg.sprite.Sprite):
  def __init__(self, groups, pos, speed, colors):
    super().__init__(groups)
    self.t0 = pg.time.get_ticks()
    self.pos = pos
    self.direction = pg.Vector2(0, 1).normalize()
    self.speed = speed
    self.particles = pg.sprite.Group()
    self.trail = pg.sprite.Group()
    self.colors = colors
    self.main_part = particle(self.particles, self.pos, choice(colors), pg.math.Vector2(0, -1), self.speed, 1000, (10, 10))
    self.exploded = False
    self.trail_timer = randint(100, 200)

  def explode(self):
    self.exploded = True
    self.particles.sprites()[0].kill()
    for x in range(500):
      particle(
        self.particles,
        self.pos.copy(),
        choice(self.colors),
        c.rand_vector(),
        randint(20, 100),
        0,
        fade = 200
      )

  def update(self, dt):
    self.pos = self.main_part.pos.copy()

    self.update_trail(dt)
    self.check_speed()
    self.check_particles()
    self.particles.update(dt)


  def update_trail(self, dt):
    self.trail.update(dt)
    if self.t0 + self.trail_timer <= pg.time.get_ticks() and not self.exploded:
      self.trail_timer += randint(10, 50)
      particle(self.trail, self.pos, choice(self.colors), c.rand_vector(), 10, 0, fade= 700)

  def check_particles(self):
    if len(self.particles.sprites()) == 0:
      self.kill()

  def check_speed(self):
    if self.main_part.speed <= 0:
      if not self.exploded:
        self.explode()

  def draw(self, surface):
    for part in self.particles:
      part.draw(surface)
    for part in self.trail:
      part.draw(surface)


class particle(pg.sprite.Sprite):
  def __init__(self, groups, pos, color, direction, speed, falloff, size = (2, 2), fade = 0) -> None:
    super().__init__(groups)
    self.pos = pos
    self.color = color
    self.direction = direction
    self.speed = speed
    self.falloff = falloff
    self.size = size
    self.lifespan = randint(100, 200)
    self.alpha = 255
    self.fade = fade
    self.define_surf()

  def define_surf(self):
    self.image = pg.Surface(self.size).convert_alpha()
    self.image.set_colorkey(c.BLACK)

    self.rect = self.image.get_rect()

    pg.draw.rect(self.image, self.color, self.rect)


  def update(self, dt):
    self.alpha -= self.fade * dt
    self.image.set_alpha(self.alpha)

    self.move(dt)
    self.check_speed(dt)
    self.check_alpha()

  def check_speed(self, dt):
    if self.speed <= 10:
      self.speed = 0
      self.falloff = 0
      # self.lifespan -= dt * 1000
      # if self.lifespan <= 0:
      #   self.kill()

  def check_alpha(self):
    if self.alpha <= 0:
      self.kill()

  def move(self, dt):
    self.pos += self.direction * self.speed * dt
    self.speed -= self.falloff * dt
    self.rect.center = self.pos

  def draw(self, surface):
    surface.blit(self.image, self.rect)