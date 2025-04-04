# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

class Asteroids:

	def __init__(self):
		self.clock = None
		self.screen = None
		self.updatables = None
		self.drawables = None
		self.dt = 0
		self.player = None

	def mainloop(self):
		while True:
			for event in pygame.event.get():
			    if event.type == pygame.QUIT:
			        return
			# updates here
			self.updatables.update(self.dt)
			# rendering nonsense beyond this point
			self.screen.fill("black")
			for drawable in self.drawables:
				drawable.draw(self.screen)
			pygame.display.flip()
			self.dt = self.clock.tick(60) / 1000

	def main(self):
		print("Starting Asteroids!")
		pygame.init()
		self.clock = pygame.time.Clock()
		self.updatables = pygame.sprite.Group()
		self.drawables = pygame.sprite.Group()
		Player.containers = (self.updatables, self.drawables)
		self.player = Player(
			SCREEN_WIDTH / 2,
			SCREEN_HEIGHT / 2
		)
		print(f"Screen width: {SCREEN_WIDTH}")
		print(f"Screen height: {SCREEN_HEIGHT}")
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.mainloop()

if __name__ == "__main__":
    game = Asteroids()
    game.main()
