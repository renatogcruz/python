# -*- coding: utf-8 -*-
"""
Created on Mon May 31 07:56:21 2021

@author: Renato

programa 6.2 - cálculo da média com notas digitadas

"""

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
cont = 0

while cont < 7:
    notas[cont] = float(input(f"Nota {cont}: "))
    soma += notas[cont]
    cont += 1
cont = 0
while cont < 7:
    print(f"Nota {cont}: {notas[cont]:6.2f}")
    cont += 1

print(f"Média: {soma / cont:5.2f}")


