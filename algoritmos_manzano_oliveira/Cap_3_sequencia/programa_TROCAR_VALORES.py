# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 08:48:38 2021

@author: Renato

ex. 4.f - ler dois valores e efetuar a troca de forma que um passe a ter o valor
do outro

"""

# Entradas
a = int(input("Entre com o valor de A: "))
b = int(input("Entre com o valor de B: "))

# Processamento
x = a
a = b
b = x

# Exibição
print(f"A = {a} e B = {b}")