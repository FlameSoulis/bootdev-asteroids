# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

pygame_clock = None
pygame_screen = None
pygame_updatables = None
pygame_drawables = None
dt = 0
player = None

def mainloop():
	global pygame_screen, pygame_clock, dt
	global pygame_updatables, pygame_drawables
	global player
	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return
		# updates here
		pygame_updatables.update(dt)
		# rendering nonsense beyond this point
		pygame_screen.fill("black")
		for drawable in pygame_drawables:
			drawable.draw(pygame_screen)
		pygame.display.flip()
		dt = pygame_clock.tick(60) / 1000

def main():
	global pygame_screen, pygame_clock
	global pygame_updatables, pygame_drawables
	global player
	print("Starting Asteroids!")
	pygame.init()
	pygame_clock = pygame.time.Clock()
	pygame_updatables = pygame.sprite.Group()
	pygame_drawables = pygame.sprite.Group()
	Player.containers = (pygame_updatables, pygame_drawables)
	player = Player(
		SCREEN_WIDTH / 2,
		SCREEN_HEIGHT / 2
	)
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	mainloop()

if __name__ == "__main__":
    main()
