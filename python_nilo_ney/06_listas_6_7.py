##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2017
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/2012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Primeira reimpressão - Segunda edição - Maio/2015
# Segunda reimpressão - Segunda edição - Janeiro/2016
# Terceira reimpressão - Segunda edição - Junho/2016
# Quarta reimpressão - Segunda edição - Março/2017
# Terceira Edição - Janeiro/2019
#
# Site: http://python.nilo.pro.br/
#
# Arquivo: exercicios\capitulo 06\exercicio-06-07.py
##############################################################################

expressao = input("Digite a sequência de parênteses a validar:")
x = 0
pilha = []
while x < len(expressao):
	if (expressao[x] == "("):
		pilha.append("(")
	if (expressao[x] == ")"):
		if (len(pilha) > 0):
			topo = pilha.pop(-1)
		else: 
			pilha.append(")") # Força a mensagem de erro
			break
	x = x + 1
if (len(pilha) == 0):
	print("Ok")
else:
	print("Erro")
