# 8.4 Parâmetros opcionais

def barra(n=40, caractere="*"):
    print(caractere * n)
    
barra()
barra(18)
barra(10, "-")

# 8.5 Nomeando os paramêtros

barra(n=10, caractere="/") # se nomeou um, é obrigatório nomear todos
barra(caractere="[", n=50) # quando nomeia, não importa a ordem

