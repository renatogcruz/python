# -*- coding: utf-8 -*-
"""
Created on Thu May  6 07:12:05 2021

@author: Renato

Exercício F - página 141

"""
# Entrada
cont = 1

# Processamento
while (cont <= 199):
    resto = cont % 4
    if resto == 0:
        print(cont)
    cont += 1
