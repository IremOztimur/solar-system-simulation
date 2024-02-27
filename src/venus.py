from planet import Planet

WHITE = (255, 255, 255)

class Venus(Planet):
	def __init__(self, x = 0.723 *  Planet.AU, y = 0, radius = 14, color = WHITE, mass = 4.8685 * 10**24):
		Planet.__init__(self, x, y, radius, color, mass)
		self.y_vel: float = -35.02 * 1000
