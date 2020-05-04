class Quadrado:

	def __init__(self, lado):
		self.lado = lado

	def perimetro(self):
		return 4 * self.lado

	def area(self):
		return self.lado * self.lado

