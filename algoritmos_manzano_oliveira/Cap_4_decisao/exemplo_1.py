# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 07:12:46 2021

@author: Renato

Exemplo 1 - elaborar um programa que efetue a entrada de um valor real não 
negativo diferente de cinco. Em caso afirmativo, apresentar sua raiz quadrada. 
Caso contrário, apresentar sua raiz cubico. Se for negativo o programa deve 
se encerrar. 

"""

# Entrada

n = float(input("Entre com valor qualquer: "))

# Processamento

if not(n < 0):
    if n != 5:
        r = n ** (1/2)
    else:
        r = n ** (1/3)

    # Exibição
    print(f"O resultado é {r}")
