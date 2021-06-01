# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 08:28:47 2021

@author: Renato

cópias e fatiamento de lista - página 100

"""

# Listas é um objeto e quando copiamos a referência se mantem
l = [1, 2, 3, 4, 5]
v = l
print("Antes")
print(f"l = {l}")
print(f"v = {v}")

v[0] = 6
print("\nDepois")
print(f"l = {l}")
print(f"v = {v}")

# para evitar isso, use outra sintaxe
l = [1, 2, 3, 4, 5]
v = l[:]
print("\nAntes")
print(f"l = {l}")
print(f"v = {v}")

v[0] = 6
print("\nDepois")
print(f"l = {l}")
print(f"v = {v}")


