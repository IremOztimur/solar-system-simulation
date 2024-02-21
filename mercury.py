from planet import Planet

DARK_GREY	= (80, 78, 81)

class Mercury(Planet):
	def __init__(self, x=0.387 * Planet.AU, y=0, radius=8, color=DARK_GREY, mass=3.30 * 10**24):
		Planet.__init__(self, x, y, radius, color, mass)
		self.y_vel =  -47.4 * 1000
