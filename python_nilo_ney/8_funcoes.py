# criando a função
def soma(a, b):
    print(a + b)
    
# chamando função
soma(2, 9)
soma(7, 8)
soma(10, 15)

# 
def somando(a, b):
    return a + b

print(somando(2, 9))

# Função que devolve verdadeiro ou falso
def ehpar(x):
    return x % 2 == 0

print(ehpar(2))
print(ehpar(7))

# função para retornar a palavra par ou ímpar
def parouimpar(x):
    if x % 2 == 0:
        return "par"
    else:
        return "ímpar"

print(parouimpar(7))
print(parouimpar(2))

# função dentro de função
def par_impar(x):
    if ehpar(x):
        return "par"
    else:
        return "ímpar"

print(par_impar(10))
print(par_impar(5))

# Exercícios
# 8.1 escreva uma função que retorne o maior de dois números
def maior(a, b):
    if a > b:
        print(a)
    else:
        print(b)

maior(5, 6)
maior(2, 1)
maior(7, 7)

# 8.2 receba dois números e retorne True se o primeiro for múltiplo
#     do segundo
def multiplo(a, b):
    if a % b == 0:
        print('True')
    else:
        print('False')

multiplo(8, 4)
multiplo(7, 3)
multiplo(5, 5)

# 8.3 receba o lado de um quadrado e retorne sua área
def quadrado(lado):
    print(f"A área do quadrado de lado {lado} é: ", lado ** 2)
          
quadrado(4)
quadrado(9)    

# 8.4 receba a base e a altura de um triângulo e retorne sua área
def triangulo(base, altura):
    print(f"Triângulo de base = {base} e altura = {altura}")
    print("Área = ", (base * altura) / 2)

triangulo(6, 9)
triangulo(5, 8)
