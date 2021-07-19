# Exercício 8.1 - pesquisa em lista - pág. 160

def pesquise(lista, valor):
    for x, e in enumerate(lista): # vai imprimir a posição do item
        if e == valor:
            return x
    return None

L = [10, 20, 25, 30]

print(pesquise(L, 10))
print(pesquise(L, 25))
print(pesquise(L, 27))

# Função enumerate
l = ['hello', 'world', 'hi', 'earth']
i = 0
while i < len(l):
    print (l[i])
    i = i + 1

l = ['hello', 'world', 'hi', 'earth']
for i, word in enumerate(l):
    print (i, word)


# calculando média
def soma(L):
    total = 0
    for e in L:
        total += e
    return total

def media(L):
    return soma(L)/len(L)

print(media([10,20,30,40]))

