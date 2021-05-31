# -*- coding: utf-8 -*-
"""
Created on Mon May 31 07:53:02 2021

@author: Renato

Programa 6.1 - cálculo da média - página 98

"""

notas = [6, 7, 5, 8, 9]

soma = 0

x = 0

while x < 5:
    soma += notas[x]
    x += 1

print(f"Média: {soma / x:5.2f}")

