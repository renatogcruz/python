# MÓDULOS, CLASSES E OBJETOS - pág 149
# Os módulos são como dicionários

import mystuff

mystuff_dic = {'apple': "I AM APPLES!"}
print(mystuff_dic['apple'])

# isso vai no mystuff.py


# def apple():
#     print("I AM APPLES!")


# # isso é apenas uma variável
# tangerine = "Living reflection of a dream"

# obtém um apple do dic
mystuff_dic['apple']
# obtém um apple do modulo
mystuff.apple()
# mesma coisa, é apenas uma variável
mystuff.tangerine

"""
Padrão no python:
1 - pegue um contêiner do tipo chave=valor
2 - obtenha algo dele usando o nome da chave

No caso do dicionário, a chave é uma string e a sintaxe é [key]. No caso
do módulo, a chave é um identificador e a sintaxe é .chave. Com excessão disso, 
são praticamente iguais.
"""


# as classes são como módulos
class MyStuff(object):

    def __init__(self):
        self.tangerine = 'Living reflection of a dream'

    def apple(self):
        print("I AM CLASSY APPLES!")


# instanciando uma classe
thing = MyStuff()
thing.apple()
print(thing.tangerine)
