from planet import Planet

YELLOW	= (253, 184, 19)

class Sun(Planet):
	def __init__(self, x=0, y=0, radius=30, color=YELLOW, mass=1.98892 * 10**30):
		Planet.__init__(self, x, y, radius, color, mass)
		self.is_sun = True
