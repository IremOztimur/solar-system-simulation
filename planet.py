import pygame
import math
import time


class Planet():
	"""
	A class representing a celestial body in a solar system simulation.

	Attributes:
		- x (float): X-coordinate of the planet's position.
		- y (float): Y-coordinate of the planet's position.
		- radius (float): Radius of the planet.
		- color (str): Color of the planet.
		- mass (float): Mass of the planet.
		- x_vel (float): X-component of the planet's velocity.
		- y_vel (float): Y-component of the planet's velocity.
		- is_sun (bool): True if the planet is the Sun, False otherwise.
		- distance_to_sun (float): Distance from the planet to the Sun.
		- orbit (list): List of positions representing the planet's orbit path.

	Constants:
		- G (float): Gravitational constant.
		- AU (float): Astronomical Unit, average distance from Earth to the Sun.
		- SCALE (float): Scaling factor for converting astronomical units to pixels.
		- TIMESTEP (float): Time increment for updating planet positions in seconds.

    Methods:
		- render(window, width, height): Render the planet on the game window.
		- attraction(other): Calculate gravitational forces between this planet and another.
		- update_position(planets): Update the planet's position based on gravitational interactions.
"""
	G = 6.67428e-11
	AU = 149.6e6 * 1000
	SCALE = 250 / AU
	TIMESTEP = 3600 * 12 # Seconds in a one day


	def __init__(self, x, y, radius, color, mass,):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.mass = mass

		self.x_vel = 0
		self.y_vel = 0

		self.is_sun = False
		self.distance_to_sun = 0
		self.orbit = []

	def render(self, window, width, height):
		x = self.x * self.SCALE + width / 2
		y = self.y * self.SCALE + height / 2

		if len(self.orbit) > 2:
			updated_points = []
			for point in self.orbit:
				x, y = point
				x = x * self.SCALE + width / 2
				y = y * self.SCALE + width / 2
				updated_points.append((x, y))
			pygame.draw.lines(window, self.color, False, updated_points, 2)

		FONT = pygame.font.SysFont("comicsans", 16)

		pygame.draw.circle(window, self.color, (x, y), self.radius)

		if not self.is_sun:
			distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, (255,255,255))
			window.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))


	def attraction(self, other):
		other_x, other_y = other.x, other.y
		distance_x = other_x - self.x
		distance_y = other_y - self.y
		distance = math.sqrt(distance_x**2 + distance_y**2)

		if other.is_sun:
			self.distance_to_sun = distance

		force = self.G * self.mass * other.mass / distance**2
		theta = math.atan2(distance_y, distance_x)
		force_x = math.cos(theta) * force
		force_y = math.sin(theta) * force
		return force_x, force_y

	def update_position(self, planets):
		total_fx = total_fy = 0
		for planet in planets:
			if self == planet:
				continue
			fx, fy = self.attraction(planet)
			total_fx += fx
			total_fy += fy

		self.x_vel += total_fx / self.mass * self.TIMESTEP
		self.y_vel += total_fy / self.mass * self.TIMESTEP

		self.x += self.x_vel * self.TIMESTEP
		self.y += self.y_vel * self.TIMESTEP
		self.orbit.append((self.x, self.y))

