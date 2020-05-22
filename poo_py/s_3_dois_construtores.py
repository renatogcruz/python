class Pessoa:

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	#construtor alternativo
	@classmethod
	def outro_construtor(cls, nome, idade):
		return cls(nome, idade)

#p = Pessoa('marcos', 20)
#print(p.nome)

#p = Pessoa.outro_construtor('pedro', 30)
#print(p.nome)

p = Pessoa.__new__(Pessoa)
dados = {'nome':'marcos', 'idade':28}
for key, value in dados.items():
	setattr(p, key, value)
print(p.nome, p.idade)