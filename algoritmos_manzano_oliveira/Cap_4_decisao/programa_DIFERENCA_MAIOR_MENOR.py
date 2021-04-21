# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 07:39:44 2021

@author: Renato

3.a - leia dois valores e apresene o resultado da diferença do maior pelo menor

"""

# Entrada
a = int(input("Entre com valor de A: "))
b = int(input("Entre com valor de B: "))

# Processamento
if a > b:
    r = a - b
else:
    r = b - a
    
# Exibição
print(f"A difenrença é de {r}")
