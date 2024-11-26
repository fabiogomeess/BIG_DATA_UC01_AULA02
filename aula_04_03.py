# Programa que realiza a soma dentre 5 números inteiros e fornece o maior entre eles
soma = 0
maior = 0
for i in range(5):
    # Início do Bloco
    num = int(input("Informe o valor:"))
    if num > maior:
        maior = num 
    soma = soma + num # Acumulador
    # Fim do Bloco
print(F"O resultado da soma é: {soma}.")
print(f"O maior valor informado é {maior}.")