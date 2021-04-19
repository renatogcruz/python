# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 07:47:00 2021

@author: Renato

Exemplo 2 - Elaborar programa que efetue a entrada de valores de medida de três 
pesos, auferidos de forma aleatória. O programa deve mostrar o maior peso 
fornecido.

"""

# Entradas
a = int(input("Entrada do valor A: "))
b = int(input("Entrada do valor B: "))
c = int(input("Entrada do valor C: "))

# Processamento
x = a
if (x < b):
    u = b
if (x < c):
    x = c

# Exibição
print(f"O maior peso é {x}")
