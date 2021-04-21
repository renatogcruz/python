# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 07:46:51 2021

@author: Renato

3.b - leia um valor e apresente como sendo positivo

"""

# Entrada
n = int(input("Entre com valor inteiro negativo ou positivo: "))

# Processamento
if n < 0:
    n = n * -1

# Exibição
print(f"O valor é {n}")