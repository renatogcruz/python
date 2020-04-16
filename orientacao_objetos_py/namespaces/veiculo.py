#criando classes

class Veiculo():
	"""Essa é a classe veiculo. Esta classe é utilizada para instanciar novos carros"""
	def __init__(self, cor, tipo_combustivel, potencia): #método init inicializa a classe
		#definido os atributos do carro
		self.__cor = cor # '__.algo' é para tornar o atributo privado (visibilidade private)
		self.__tipo_combustivel = tipo_combustivel
		self.__potencia = potencia
		self.__qtd_combustivel = 0
		self.__is_ligado = False
		self.__velocidade = 0

	def __del__(self):
		print("O objeto foi removido da memória.")

	def abastecer(self, qtd_combustivel):
		"""O método abastecer recebe como parametros a quantidade de combustível e incrementa a nova quantidade de combustível"""
		print(f"O carro possui {self.__qtd_combustivel} litros de combustível")
		self.__qtd_combustivel += qtd_combustivel

	def ligar(self):
		if self.__is_ligado:
			print("O carro já está ligado.")
		else:
			self.__is_ligado = True
			print("O carro foi ligado.")

	def desligar(self):
		if self.__is_ligado == False:
			print("O carro já está desligado.")
		else:
			self.__is_ligado = False
			print("O carro foi desligado.")

	def acelerar(self, velocidade=10):
		if self.__is_ligado:
			self.__velocidade += velocidade
		else:
			print("O carro precisa ser ligado para acelerar.")



