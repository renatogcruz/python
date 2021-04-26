# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 07:34:24 2021

@author: Renato

Ex. 3. j - página 109

"""

# Entrada
n = int(input("Entre com valor: "))

# Processamento
resto2 = n % 2
if resto2 == 0:
    print(f"{n} é par!")
else:
    print(f"{n} é ímpar!")
