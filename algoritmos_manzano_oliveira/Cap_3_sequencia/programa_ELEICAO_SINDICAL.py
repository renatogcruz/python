# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 07:39:21 2021

@author: Renato

4.r - programa eleição sindical (página 66)

"""

# Entrada
va = int(input("Entre com quantidade votos em A: "))
vb = int(input("Entre com quantidade votos em B: "))
vc = int(input("Entre com quantidade votos em C: "))
nl = int(input("Entre com quantidade votos nulos: "))
br = int(input("Entre com quantidade votos brancos: "))

# Processamento
total = va + vb + vc + nl + br
p_validos = (va + vb + vc) * 100 / total
p_a = va * 100 / total
p_b = vb * 100 / total
p_c = vc * 100 / total
p_nl = nl * 100 / total
p_br = br * 100 / total

# Exibição
print(f"Votos total  = {total}")
print(f"Votos válidos  = {p_validos}")
print(f"Votos A  = {p_a}")
print(f"Votos B  = {p_b}")
print(f"Votos C  = {p_c}")
print(f"Votos Nulos  = {p_nl}")
print(f"Votos Brancos  = {p_br}")

         