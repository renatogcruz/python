"""
Se um objeto anda como um pato e faz quack como um pato então
ele é um pato
"""
class Pato:

	def quack(self):
		print("Quack, quack")

class Pessoa:

	def quack(self):
		print("Eu faço quack igual a um pato")

"""
#isso NÃO é pythonico
def fazer_quack(algo):

	if isinstance(algo, Pato):
		algo.quack()
	else:
		print("Isso tem que ser um pato")
"""
"""
def fazer_quack(obj):
	#LBYL - NÃO é pythonico
	if hasattr(obj, 'quack'):
		if callable(obj.quack):
			obj.quack()
"""

def fazer_quack(obj):
	# EAFP - Easier to ask for forgiveness than permission (pythonico)
	try:
		obj.quack()
	except AttributeError as e:
		print(e)




pato = Pato()
fazer_quack(pato)

pessoa = Pessoa()
fazer_quack(pessoa)



"""
class Livro():

	def __init__(self, titulo, lancamento, autor):
		self.titulo = titulo
		self.lancamento = lancamento
		self.autor = autor


class Filme():

	def __init__(self, titulo, lancamento, diretor):
		self.titulo = titulo
		self.lancamento = lancamento
		self.diretor = diretor

def imprimir(midia):
	print(midia.titulo, midia.lancamento)
"""