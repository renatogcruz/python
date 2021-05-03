# -*- coding: utf-8 -*-
"""
Created on Mon May  3 07:18:05 2021

@author: Renato

Ex. B - página 141

"""

# Entrada
n = int(input("Entre com o número: "))

# Processamento
cont = 0

while cont <= 10:
    tab = n * cont
    print(f'{n} x {cont} = {tab}')
    cont += 1