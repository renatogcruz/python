# -*- coding: utf-8 -*-
"""
Created on Tue May  4 08:30:51 2021

@author: Renato

Ex. D - página 141

"""
cont = 1
soma = 0

# Processamento
while cont <= 500:    
    resultado = cont % 2
    if resultado == 0:
        soma += cont
    cont += 1
    
# Exibição
print(f"A soma dos pares de 1 a 500 é igual a {soma}")
    