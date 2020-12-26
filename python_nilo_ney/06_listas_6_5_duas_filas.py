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
# Arquivo: exercicios\capitulo 06\exercicio-06-06.py
##############################################################################

ultimo = 0
fila1 = []
fila2 = []
while True:
     print("\nExistem %d clientes na fila 1 e %d na fila 2." % (len(fila1), len(fila2)))
     print("Fila 1 atual:", fila1)
     print("Fila 2 autal:", fila2)
     print("Digite F para adicionar um cliente ao fim da fila 1 (ou G para fila 2),")
     print("ou A para realizar o atendimento a fila 1 (ou B para fila 2")
     print("S para sair.")
     operacao = input("Operação (F, G, A, B ou S):")
     x=0
     sair = False
     while x < len(operacao):
         # Aqui vamos usar fila como referência a fila 1
         # ou a fila 2, dependendo da operação.
         if operacao[x] == "A" or operacao[x] == "F":
            fila = fila1
         else:
            fila = fila2
         if operacao[x] == "A" or operacao[x]=="B":
             if(len(fila))>0:
                   atendido = fila.pop(0)
                   print("Cliente %d atendido" % atendido)
             else:
                   print("Fila vazia! Ninguém para atender.")
         elif operacao[x] == "F" or operacao[x]=="G":
             ultimo += 1 # Incrementa o ticket do novo cliente
             fila.append(ultimo)
         elif operacao[x] == "S":
             sair = True
             break
         else:
             print("Operação inválida: %s na posição %d! Digite apenas F, A ou S!" % (operacao[x],x))
         x = x + 1
     if(sair):
        break