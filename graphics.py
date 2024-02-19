import pygame

class Graphics:
	def __init__(self, WIDTH, HEIGHT):
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT
		self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		
		pygame.display.set_caption("Planet Simulation")

