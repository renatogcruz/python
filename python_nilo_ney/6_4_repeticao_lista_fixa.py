# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 08:38:52 2021

@author: Renato

programa 6.4 repetição com tamanho fixo de lista

"""

L = [1, 2, 3]
x = 0

while x < 3:
    print(L[x])
    x += 1

L = [1, 2, 3]
x = 0

while x < len(L):
    print(L[x])
    x += 1

# Adição de elementos

L = []
L.append("a")
print(L)

# Programa 6.6
L = []
while True:
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n)

x = 0
while x < len(L):
    print(L[x])
    x += 1

# extend - adiciona os elementos de uma lista em outra
L = ["a"]
L.append("b")

L.extend(["c"])  # extend não aceita parametros que não sejam listas
print(L)

# leia duas lista e faça uma terceira

L = [1, 2, 3]
M = [2, 4, 5]

N = L[:]
N.extend(M)

print(N)

# del - retira elemeto de lista






