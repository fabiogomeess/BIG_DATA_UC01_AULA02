# ANALISE DE HABITANTES
def analise_de_habitantes():
    maior_idade = 0
    qtd_f = 0
    qtd_olhos = 0

habitantes = int(input("Informe o número de habitantes: "))

for i in range(habitantes):
    print("Informe as características dos habitantes: ")

    sexo = input("Informe o sexo (M ou F): ")
    olho = input("Informe a cor dos olhos (azuis, verdes ou castanhos): ")
    cabelo = input("Informe a cor do cabelo (loiros, castanhos ou pretos: ")
    idade = int(input("Informe a idade: "))

    if idade > maior_idade:
        maior_idade = idade

    if sexo == "F" and 18 <= idade <= 35:
        qtd_f =+ 1

    if (olho == "verdes") and (cabelo == "louro"):
        qtd_olhos = 0

print(maior_idade)
print(qtd_f)
print(qtd_olhos)