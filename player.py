from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.containers = None
		self.shoot_timer = 0

	# in the player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		bullet = Shot(self.position.x, self.position.y)
		bullet.position += pygame.Vector2(0,PLAYER_RADIUS).rotate(self.rotation)
		bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation)
		bullet.velocity *= PLAYER_SHOOT_SPEED

	def update(self, dt):
		self.shoot_timer -= dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
			self.shoot_timer = PLAYER_SHOOT_COOLDOWN
			self.shoot()
