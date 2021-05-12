# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:07:06 2021

@author: Renato

Exercício M - página 142

"""

# Entrada
c = 0
s = 0

# Processamento
while (c <= 10):
    n = int(input("Entre com valor: "))
    s = s + n
    c = c + 1
    
m = s / 10

# Exibição
print(f"Soma = {s}. Média = {m}")