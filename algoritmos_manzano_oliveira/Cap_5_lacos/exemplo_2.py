# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 07:57:44 2021

@author: Renato

Exemplo 2 - página 137

"""

# Inputs
fat = 1
cont = 1

# processsamento
while not cont > 5:
    fat = fat * cont
    cont = cont + 1
    
# exibição
print(f"5! = {fat}")
