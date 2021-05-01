# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:42:43 2021

@author: Renato
"""

tabuada = 1
numero = 1

while tabuada <= 10:    
    print(f'{tabuada} x {numero} = {tabuada * numero}')    
    numero += 1
    
    if numero == 11:
        print('\n')
        numero = 1
        tabuada += 1