"""
Faça um programa que leia duas listas e que gere
uma terceira sem elementos repetidos
"""

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
c = []

contador = 0

while contador < len(a):	
	print(a[contador])
	print(b[contador])
	c.append(a[contador])
	if b[contador] != a[contador]:
		c.append(b[contador])
	contador += 1
	

print(c)

