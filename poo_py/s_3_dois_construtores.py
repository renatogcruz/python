class Pessoa:

	def __init__(self, nome):
		self.nome = nome

	#construtor alternativo
	@classmethod
	def outro_construtor(cls, nome):
		return cls(nome)

#p = Pessoa('marcos')
#print(p.nome)

p = Pessoa.outro_construtor('pedro')
print(p.nome)