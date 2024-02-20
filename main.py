from planet import Planet
from graphics import Graphics
from random import randint
import pygame
import math

pygame.init()

simulation = Graphics(800, 800)

##### COLOR CODES #####
WHITE		= (255, 255, 255)
BLACK		= (0, 0, 0)
RED			= (188, 39, 50)
BLUE		= (100, 149, 237)
YELLOW		= (253, 184, 19)
DARK_GREY	= (80, 78, 81)

def	main():
	gameOn = True
	clock = pygame.time.Clock()

	sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
	sun.is_sun = True

	earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
	earth.y_vel = 29.783 * 1000 # meters per sec

	mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
	mars.y_vel = 24.077 * 1000

	mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**24)
	mercury.y_vel = -47.4 * 1000

	venus = Planet(0.723 *  Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
	venus.y_vel = -35.02 * 1000

	planets = [sun, earth, mars, mercury, venus]

	stars = [((randint(150, 200), randint(150, 200), randint(150, 200)), (randint(1, simulation.WIDTH), randint(1, simulation.HEIGHT)), randint(1, 2)) for _ in range(250)]
	def draw_stars():
		for star in stars:
			pygame.draw.circle(simulation.WIN, star[0], star[1], star[2])

	while gameOn:
		clock.tick(60)
		simulation.WIN.fill(BLACK)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOn = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gameOn = False
		for planet in planets:
			draw_stars()
			planet.update_position(planets)
			planet.render(simulation.WIN, simulation.WIDTH, simulation.HEIGHT)

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()
