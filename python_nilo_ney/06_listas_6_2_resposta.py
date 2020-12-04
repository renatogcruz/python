##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2020
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: exercicios3\capitulo 06\exercicio-06-02.py
##############################################################################

primeira = [1, 2, 3, 4, 5]
segunda = [6, 7, 8, 9, 0]
contador = 0
while contador < len(primeira):
	print(primeira[contador])
	print(segunda[contador])
	contador += 1

terceira = primeira[:]
terceira.extend(segunda)

print(terceira)


