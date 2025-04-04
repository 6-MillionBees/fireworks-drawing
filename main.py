# Arden Boettcher
# 3/7/25
# Fireworks Drawing

import pygame
import config as c
import firework as fire

from random import randint, choice

pygame.init()




# Main loop
def main():

  # Setting up the window
  screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
  pygame.display.set_caption("PLACEHOLDER")

  # Delta Time
  dt = 0

  # Firework Group
  fireworks = pygame.sprite.Group()

  # Setting up the clock
  clock = pygame.time.Clock()
  pygame.time.set_timer(c.CALL_FIREWORK, randint(200, 1000))

  # The bool for the main loop
  running = True

  while running:

    # Call events / update running
    for event in pygame.event.get():
      # Quits the game when you press the x
      if event.type == pygame.QUIT:
        return
      if event.type == c.CALL_FIREWORK:
        pygame.time.set_timer(c.CALL_FIREWORK, randint(200, 1000))
        if randint(0, 10):
          fire.Firework(fireworks, [randint(0, c.WIDTH), c.HEIGHT], randint(750, 900), c.RED_FIREWORK)
        else:
          fire.Miku_Work(fireworks, [randint(0, c.WIDTH), c.HEIGHT], randint(750, 900))

    fireworks.update(dt)

    # Fills window
    screen.fill(c.ALLMOST_BLACK)

    for firework in fireworks:
      firework.draw(screen)


    draw_foreground(screen)

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    dt = clock.tick(c.FPS) / 1000

  # Close the pygame modules
  pygame.quit()



def draw_foreground(surface):
  for rect in c.FOREGROUND_RECTS:
    pygame.draw.rect(surface, c.BLACK, rect)



# Calls the code
if __name__ == "__main__":
  main()
