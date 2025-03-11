# Arden Boettcher
# Insert date here
# Insert title here

from pygame import Rect, event
from pygame.math import Vector2
from random import randint
import math


# Screen size constants
WIDTH = 500
HEIGHT = 500

# Framerate
FPS = 60

# Color Constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
ORANGE = (255, 60, 0)
YELLOW = (255, 183, 0)
GREEN = (0, 255, 0)
MIKU = (0, 255, 208)
BLUE = (0, 0, 255)

CALL_FIREWORK = event.custom_type()

RED_FIREWORK = [RED, ORANGE, YELLOW]
# GREEN_FIREWORK = []

FOREGROUND_RECTS = [
  Rect(0, 292, 44, 208),
  Rect(44, 258, 46, 242),
  Rect(90, 398, 41, 102),
  Rect(131, 308, 59, 192),
  Rect(190, 355, 30, 155),
  Rect(220, 397, 49, 103),
  Rect(269, 367, 52, 133),
  Rect(321, 374, 42, 126),
  Rect(363, 267, 55, 233),
  Rect(418, 247, 42, 253),
  Rect(460, 316, 40, 184),
]

def rand_vector():
  angle = math.radians(randint(0, 360))
  x = math.cos(angle)
  y = math.sin(angle)
  return Vector2(x, y).normalize()