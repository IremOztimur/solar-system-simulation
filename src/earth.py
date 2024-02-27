from planet import Planet

BLUE = (100, 149, 237)

class Earth(Planet):
	def __init__(self, x=-1 * Planet.AU, y=0, radius=16, color=BLUE, mass=5.9742 * 10**24):
		Planet.__init__(self, x, y, radius, color, mass)
		self.y_vel =  29.783 * 1000
