class P():

	def __init__(self, x):
		self.x = x

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		if x > 0:
			self._x = x
	

"""
NÃO é pythonico

	def getX(self):
		return self.__x

	def setX(self, x):
		if x > 0:
			self.__x = x

p = P(10)
print(p.getX())
p.setX(1)
print(p.getX())
"""

p = P(10)
print(p.x)
p.x = -1
print(p.x)

