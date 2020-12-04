z = [15, 8, 9]

print(z)
print(z[0])

z[0] = 7
print(z)
print(z[0])

#cálculo da média
notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
	soma += notas[x]
	x += 1

print(f"\nMédia: {soma / x:5.2f}")