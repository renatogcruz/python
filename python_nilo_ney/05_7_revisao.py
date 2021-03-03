# -*- coding: utf-8 -*-

# 5.7 - repetições taboada


n = int(input("Tabuada de: ")) 
inicio = int(input("Entre com o início: "))
fim = int(input("Entre com o fim: "))


while inicio <= fim:
    print(f"{n} x {inicio} = {n * inicio}")
    inicio += 1


# 5.8 2 numeros multiplicados utilizando soma
number1 = int(input("Entre com o primeiro número:  "))
number2 = int(input("Entre com o segundo número:  "))

cont = 1
soma = 0

while cont <= number1:    
    soma += number2
    cont += 1

print("Resultado é ", soma)
    
    

