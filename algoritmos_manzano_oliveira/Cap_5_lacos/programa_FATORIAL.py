# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:08:51 2021

@author: Renato

Exercício - página 142

"""
# Entrada
i = 1

# processamento
while (i <= 10):
    r = i % 2
    if r != 0:
        fat = 1
        j = 1
        while (j <= i):            
            fat = fat * j
            j = j +1
        print(f"{i}! = {fat}")
    
    i = i + 1
            

