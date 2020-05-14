class Pessoa:
	__slots__ = ['nome', 'idade', 'peso']
	def __init__(self, nome, idade, peso):
		self.nome = nome
		self.idade = idade
		self.peso = peso
		