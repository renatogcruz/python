# 8.1 - Variáveis locais e globais

EMPRESA = "Unidos Venceremos LTDA" # variável global

def imprime_cabecalho():
    print(EMPRESA)
    print("-" * len(EMPRESA))
    
imprime_cabecalho()

# O bom uso de variáveis globais e guardar valores constantes
# e que devem ser acessíveis a todas as funções do programa

# Tente usar variáveis globais apenas para configurações e com
# valores constantes

a = 5 # variável global
def muda_e_imprime():
    a = 7
    print(f"A dentro da função: {a}")
print(f"A antes de mudar: {a}")

muda_e_imprime()
print(f"A depois de mudar: {a}")    
    

b = 5                                 # variável global
def muda():
    global b                          # cria variável global dentro da função
    b = 7
    print(f"B dentro da função: {b}")
print(f"B antes de mudar: {b}")
muda()
print(f"B depois de mudar: {b}")








    