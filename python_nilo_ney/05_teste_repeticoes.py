## pag. 88 exemplo correção de teste

pontos = 0
questao = 1

while questao <= 3:
    resposta = str(input(f"Resposta da questão {questao}: "))
    if questao == 1 and resposta == 'b':
        pontos += 1
    if questao == 2 and resposta == 'a':
        pontos += 1
    if questao == 3 and resposta == 'd':
        pontos += 1
    questao += 1

print(f"\nO aluno fez {pontos} ponto(s)")

## 5.10 exemplo correção de teste com maiúsculas e minúsculas

pontos = 0
questao = 1

while questao <= 3:
    resposta = str(input(f"Resposta da questão {questao}: "))
    if questao == 1 and (resposta == 'b' or resposta == 'B'):
        pontos += 1
    if questao == 2 and (resposta == 'a' or resposta == 'A'):
        pontos += 1
    if questao == 3 and (resposta == 'd' or resposta == 'D'):
        pontos += 1
    questao += 1

print(f"\nO aluno fez {pontos} ponto(s)")
