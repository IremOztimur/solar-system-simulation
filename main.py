from planet import Planet
from universe import Universe
from sun import Sun
from earth import Earth
from mars import Mars
from mercury import Mercury
from venus import Venus
import pygame
import math

pygame.init()

universe = Universe(800, 800)

##### COLOR CODES #####
BLACK		= (0, 0, 0)

def	main():
	gameOn = True
	clock = pygame.time.Clock()

	sun = Sun()
	earth = Earth()
	mars = Mars()
	mercury = Mercury()
	venus = Venus()

	planets = [sun, earth, mars, mercury, venus]

	while gameOn:
		clock.tick(60)
		universe.WIN.fill(BLACK)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOn = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gameOn = False
		for planet in planets:
			universe.draw_stars()
			planet.update_position(planets)
			planet.render(universe.WIN, universe.WIDTH, universe.HEIGHT)

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()
