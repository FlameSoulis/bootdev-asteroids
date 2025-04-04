# it cost $400000 to fire this weapon for 12 seconds
from circleshape import *
from constants import *

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, screen):
		pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt