from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

	@abstractmethod
	def dizer_algo(self):
		pass

class Cachorro(Animal):
	def dizer_algo(self):
		return 'AU AU'

c = Cachorro()
print(c.dizer_algo())