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


#trabalhando com índice
print(notas[2])
print(notas[0])

#cópia e fatiamento de listas
L = [1, 2, 3, 4, 5]
V = L      #primeira sintaxe para copiar

print("")
print(L)
print(V)
V[0] = 6
print(L)
print(V)

V = L[:]   #segunda sintaxe para copiar
V[0] = 15
print("")
print(V)
print(L)

print("")
print(L[:2])
print(L[1:2])

print(f"Tamanho da lista: {len(L)}")

contador = 0
while contador < len(L):
	print(L[contador])
	contador += 1

#adição de elementos
print("")
M = []
print(M)
M.append("a")
M.append("b")
print(M)
M.append("c")
print(M)

print("")
M = M + ["d"] #outra forma de adicionar elementos numa lista
print(M)
M += ["e"]
print(M)





