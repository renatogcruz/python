"""
PEP 257 -- Docstring Conventions

https://www.python.org/dev/peps/pep-0257/
"""

def multiplicar(x, y):
	"""Essa função retorna a multiplicação de dois números"""
	return x * y


help(multiplicar)

print(multiplicar(2, 4))