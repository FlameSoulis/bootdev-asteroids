# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

pygame_clock = None
pygame_screen = None
dt = 0
player = Player(
	SCREEN_WIDTH / 2,
	SCREEN_HEIGHT / 2
)

def mainloop():
	global pygame_screen, pygame_clock, dt
	global player
	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return
		pygame_screen.fill("black")
		player.draw(pygame_screen)
		pygame.display.flip()
		dt = pygame_clock.tick(60) / 1000

def main():
	global pygame_screen, pygame_clock
	global player
	print("Starting Asteroids!")
	pygame.init()
	pygame_clock = pygame.time.Clock()
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	mainloop()

if __name__ == "__main__":
    main()
