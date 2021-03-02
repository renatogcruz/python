# -*- coding: utf-8 -*-

# 5 - repetições

"""
while <condição>:
    bloco
"""

x = 1
while x <= 3:
    print(x)
    x += 1
    
    
# 4.3 - lançamento de um foguete

print("Programa para contagem regressiva. Lançamento de foguete.")
contagem = 10

while contagem >= 0:
    print(contagem)
    contagem -= 1
print("Fogo!")
    
# 5.1 Contadores
fim = int(input("Entre com o último número a imprimir: "))
x = 1
while x <= fim:
    if x % 2 == 0:
        print(x)
    x += 1

# 5.2 Contadores
fim = int(input("Entre com o último número a imprimir: "))
x = 1
while x <= fim:
    if x % 2 != 0:
        print(x)
    x += 1

# 5.5 10 primeiros multiplos de 3

multiplos = 0
while multiplos <= 30:    
    if multiplos % 3 == 0:
        print(multiplos)
    multiplos += 1
    
print("")

n = int(input("Tabuada de: ")) 
x = 1
while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x += 1




