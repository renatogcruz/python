print(10 + 10)
print(10 .__add__(10))

class Operador():
	def __init__(self, num):
		self.num = num
	def __add__(self, op):
		return self.num - op.num
	def __mul__(self, op):
		return self.num ** op.num
	def __sub__(self, op):
		return self.num + op.num

op = Operador(10)
op2 = Operador(2)

print(op + op2)
print(op * op2)
print(op - op2)
