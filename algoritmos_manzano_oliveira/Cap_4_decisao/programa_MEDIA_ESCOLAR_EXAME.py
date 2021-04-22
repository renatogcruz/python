# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 07:17:31 2021

@author: Renato

Ex. 3.d - página 109

"""

# Entrada 
a = float(input("Entre com a primeira nota: "))
b = float(input("Entre com a segunda nota: "))
c = float(input("Entre com a terceira nota: "))
d = float(input("Entre com a quarta nota: "))

# Processamento
media = (a+b+c+d)/4

if media >= 7:
    print("Aprovado")
else:
    e = float(input("Entre com a nota do exame: "))
    media_2 = (media + e) / 2
    if media_2 >= 5:
        print("Aprovado Exame Especial")
    else:
        print("Reprovado")
        
