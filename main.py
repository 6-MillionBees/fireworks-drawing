# Arden Boettcher
# 3/7/25
# Fireworks Drawing

import pygame
import config
pygame.init()


# Event handling
def main_events():
  for event in pygame.event.get():
    # Quits the game when you press the x
    if event.type == pygame.QUIT:
      return False
  return True



# Main loop
def main():

  # Setting up the window
  screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
  pygame.display.set_caption("PLACEHOLDER")

  # Setting up the clock
  clock = pygame.time.Clock()

  # The bool for the main loop
  running = True

  # A few misc things
  # overlay = pygame.Surface()

  while running:

    # Call events / update running
    running = main_events()

    # Fills window
    screen.fill(config.WHITE)

    draw_foreground(screen)

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    clock.tick(config.FPS)

  # Close the pygame modules
  pygame.quit()


def draw_foreground(surface):
  for rect in config.FOREGROUND_RECTS:
    pygame.draw.rect(surface, config.BLACK, rect)

def draw_background(surface):
  cloud = pygame.Surface(100, 70)


# Calls the code
if __name__ == "__main__":
  main()
