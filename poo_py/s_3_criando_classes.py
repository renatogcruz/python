class MinhaClasse:
	pass            #pass indica que nenhuma outra ação precisa ser tomada

obj = MinhaClasse()

print(type(obj))

class Ponto:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def resetar(self):
		self.x, self.y = 0, 0


p = Ponto(10, 20)
print(p.x, p.y)

p.resetar()
print(p.x, p.y)

