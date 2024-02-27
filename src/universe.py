import pygame
from random import randint


class Universe:
	def __init__(self, WIDTH: int, HEIGHT: int):
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT
		self.WIN: pygame.surface.Surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.stars = [((randint(150, 200), randint(150, 200), randint(150, 200)), (randint(1, self.WIDTH), randint(1, self.HEIGHT)), randint(1, 2)) for _ in range(250)]
		pygame.display.set_caption("Solar System Simulation")

	def draw_stars(self):
		for star in self.stars:
			pygame.draw.circle(self.WIN, star[0], star[1], star[2])
