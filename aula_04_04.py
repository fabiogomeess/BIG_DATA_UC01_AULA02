# Programa para calcular a soma e a média da idade de 10 pessoas 
soma = 0
media = 0
num_maior = 0
nome_maior = ""
for i in range(3):
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    if idade > num_maior:
        num_maior = idade
        nome_maior = nome
    soma = soma + idade
media = soma / (i + 1) # é porque o i inicia com o valor 0, desta forma iniciará com 1 (i+1)
print(f"A soma das idades é {soma} e a média é {media:.0f}")
print(f"A pessoa mais velha é {nome_maior}")
