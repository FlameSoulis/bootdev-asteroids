# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from constants import *
from player import *
from asteroidfield import *

class AsteroidsGame:

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
			for obj in self.asteroids:
				if obj.collision_check(self.player):
					print("Game over!")
					sys.exit(0)
				for bullet in self.bullets:
					if obj.collision_check(bullet):
						obj.split()
						bullet.kill()
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
		self.asteroids = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		Player.containers = (self.updatables, self.drawables)
		Asteroid.containers = (self.asteroids, self.updatables, self.drawables)
		AsteroidField.containers = (self.updatables)
		Shot.containers = (self.bullets, self.updatables, self.drawables)
		self.asteroid_field = AsteroidField()
		self.player = Player(
			SCREEN_WIDTH / 2,
			SCREEN_HEIGHT / 2
		)
		print(f"Screen width: {SCREEN_WIDTH}")
		print(f"Screen height: {SCREEN_HEIGHT}")
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.mainloop()

if __name__ == "__main__":
    game = AsteroidsGame()
    game.main()
