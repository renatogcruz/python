# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 08:54:02 2021

@author: Renato

Apresentar o volume de uma lata de óleo
"""

# entradas
r = float(input("Entre com o raio da lata: "))
h = float(input("Entre com a altura da lata: "))

# processamento
v = 3.14 * r ** 2 * h

# exibição
print(f"O volume da lata é de {v}")
