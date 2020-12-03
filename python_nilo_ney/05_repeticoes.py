#caso while

x = 1
while x <= 3:
	print(x)
	x += 1

#exercicios
#5.1, 5.2
x = 50
while x <= 55:
	print(x)
	x += 1

#5.3
x = 10
while x >= 1:
	print(x)
	x = x - 1

print("\n")

fim = 10
x = 0
while x <= fim:
	if x % 2 == 0:
		print(x)
	x += 1

y = 0
while y <= 30:
	print(y)
	y += 3

print("tabuada")
n = 5
x = 1
while x <= 10:
	print(f"{n} x {x} = {n * x}")
	x += 1

#acumuladores
import random

x = 1    #x é um contador porque seu valor adicionado é constante
soma = 0 #soma é um acumulador pois o valor adicionado é variável
while x <= 5:
	n = random.randint(1, 10)
	soma += n
	x += 1
	print(soma)

print("tabuadas")
tabuada_ = 1
while tabuada_ <= 10:
	numero = 1                 #é a inicialização da variavel número pq precisamos voltar a multiplicar por 1
	print(f"\nTabuada do {tabuada_}")
	while numero <= 10:
		print(f"{tabuada_} x {numero} = {tabuada_ * numero}")
		numero += 1
	tabuada_ += 1
		

#f string é muito legal
preco = 5.20
print(f"\nPreço: {preco:5.2f}") #pula linhas entre os dois pontos e valores a ser impresso
print(f"\nPreço: {preco:15.2f}")
print(f"\nPreço: {preco:.2f}")

print(f"\nPreço R$:{preco:.^10.2f}")
print(f"\nPreço R$:{preco:*^10.2f}")
print(f"\nPreço R$:{preco:.^10.2f}")
