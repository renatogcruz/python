import math

class Forma():
	"""
	http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html
	"""

	def __init__(self):
		print("Construtor da forma")

	def area(self):
		print("Área da forma")

	def perimetro(self):
		print("Perimetro da forma")

	def descricao(self):
		print("Descricao da forma")

class Quadrado(Forma):

	def __init__(self, lado):
		self.lado = lado

	def area(self):
		return self.lado ** 2

	def perimetro(self):
		return self.lado * 4

class Circulo(Forma):
	
	def __init__(self, raio):
		self.raio = raio

	def area(self):
		return math.pi * self.raio ** 2

	def perimetro(self):
		return 2 * math.pi * self.raio

	def descricao(self):
		print('Descrição do ciruclo')

quad = Quadrado(2)
print('Área: %d ' % quad.area())
print('Perimetro: %d' %quad.perimetro())
quad.descricao()

circ = Circulo(2)
print('Área: %d ' % circ.area())
print('Perimetro: %d' %circ.perimetro())
circ.descricao()