from planet import Planet

RED	= (188, 39, 50)

class Mars(Planet):
	def __init__(self, x=-1.524 * Planet.AU, y=0, radius=12, color=RED, mass=6.39 * 10**23):
		Planet.__init__(self, x, y, radius, color, mass)
		self.y_vel =  24.077 * 1000
