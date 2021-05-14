# -*- coding: utf-8 -*-
"""
Created on Fri May 14 08:24:46 2021

@author: Renato

Exercicio P - página 142

"""

# Entrada
soma = 0
qua_num = 0
contador = 50

# Processamento
while (contador <= 70):
    soma = soma + contador
    contador = contador + 1
    qua_num = qua_num + 1

media = soma / qua_num
    
# Exibição
print(f"Soma = {soma}\nMédia = {media}")
