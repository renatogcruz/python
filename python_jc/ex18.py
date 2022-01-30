# Nomes, variáveis, código, funções - agora sim
# página 63

'''
As funções fazem 3 coisas: 
* nomeiam partes do código, assim como as variáveis nomeiam strings e números;
* recebem argumentos da mesma maneira que seus scripts recebem argv;
* usando 1 e 2, permitem que vc crie seus próprios 'miniscripts' ou pequenos
comandos.
'''


def print_two(*args):
    # igual as scripts com argv
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# o argumento *args, em python, nos informa que todos os argumentos para a função serão colocados
# em uma lista. Não é usado com muita frequência


def print_two_again(arg1, arg2):
    # aquele *argv é desnecessário
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg1):
    # print apenas 1 argumento
    print(f"arg1: {arg1}")


def print_none():
    # print apenas 1 argumento
    print("I got nothin..")


print_two('Renato', 'Cruz')
print_two_again('Godoi', 'Cruz')
print_one('Renato')
print_none()
