# -*- coding: utf-8 -*-

# 4.4 - carro novo ou velho com else

idade = int(input("Digite a idade de seu carro: "))

if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")



# 4.6 viagem
distancia = int(input("Qual distância vc pretende viajar: "))

if distancia <= 200:
    preco = distancia * 0.50
    print(f"Preço da viagem é de R$ {preco:6.2f}")
else:
    preco = distancia * 0.45
    print(f"Preço da viagem é de R$ {preco:6.2f}")

# 4..5 - conta de telefone com 3 faixas de preço
minutos = int(input("Quantos minutos você utilizou este mês: "))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print(f"Você vai pagar este mês: R$ {minutos * preco:6.2f}")

# 4.6 - categoria x preço
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print("Categória inválida")
                    preco = 0
print(f"O preço do produto é: R$ {preco:6.2f}")

# 4.7 - categoria x preço com elif
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categória inválida")
    preco = 0
print(f"O preço do produto é: R$ {preco:6.2f}")









