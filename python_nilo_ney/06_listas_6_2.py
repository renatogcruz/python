"""
Faça um programa que leia duas listas e que gere
uma terceira com os elementos das duas
"""

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]

contador = 0

while contador < len(a):	
	print(a[contador])
	print(b[contador])
	contador += 1
	
a.extend(b)	
print(a)

