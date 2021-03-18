# 5.2 Acumuladores

"""
A diferença entre um contador e um acumulador é que nos contadores
o valor adicionado é constante e, nos acumuladores, variável
"""

n = 1
soma = 0

while n <= 10:
    x = int(input(f"Digite o {n} número: "))
    soma = soma + x                          # é um acumulador
    n = n + 1                                # é um contador
    
print(f"Soma: {soma}")

# programa para calcular cinco variáveis

print("\nPrograma para calcular 5 variáveis")

x = 1
soma = 0

while x <= 5:
    n = int(input(f"{x} Digite o número: "))
    soma = soma + n                          #
    x = x + 1
print(f"Média: {soma / 5:5.2f}")

# Exercícios

# 5.11 programa poupança

print("\nPrograma Poupança")

deposito = float(input("Entre com valor depositado: "))
taxaJuros = float(input("Entre com valor da taxa de jutos: "))
print(f"Valor depositado: R$ {deposito:5.2f} e taxa de jutos {taxaJuros} %")

valor = deposito
taxa = taxaJuros
ganhoTotal = 0
meses = 24
cont = 1

while cont <= meses:
    ganho = valor + (valor * taxa / 100)
    print(f"O ganho do mês {cont} foi de R$ {ganho:5.2f}")
    ganhoTotal += ganho
    cont += 1

print(f"O ganho total em 24 foi de R$ {ganhoTotal:5.2f}")

