# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 08:14:00 2021

@author: Renato

Ex. 3.g - página 109

"""

# Entrada
a = int(input("Entre com valor de A: "))
b = int(input("Entre com valor de B: "))
c = int(input("Entre com valor de C: "))
d = int(input("Entre com valor de D: "))

# Processamento
resto2 = a % 2
resto3 = a % 3
if (resto2 == 0) and (resto3 == 0):
    print(a)

resto2 = b % 2
resto3 = b % 3
if (resto2 == 0) or (resto3 == 0):
    print(b)

resto2 = c % 2
resto3 = c % 3
if (resto2 == 0) or (resto3 == 0):
    print(c)

resto2 = d % 2
resto3 = d % 3
if (resto2 == 0) or (resto3 == 0):
    print(d)




