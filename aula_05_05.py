#
resposta = ["B","B","B","D","E"]
gabarito = ["A","B","B","D","E"]
acertos = 0
erros = 0
for i in range(len(resposta)):
    if resposta[i] == gabarito[i]:
        acertos += 1
    else:
        erros +=1
print(resposta)
print(gabarito)
print(f"A quantidade de acertos foi: {acertos}")
print(f"A quantidade de erros foi: {erros}")

    