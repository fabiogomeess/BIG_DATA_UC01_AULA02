# Programa para tratar o erro da escrita 
nome = input("Informe seu nome: ")
while True:
  sexo = input("Informe seu sexo (M ou F): ")
  if sexo == "M" or sexo == "F":
    break
  else:
    print("Informe apenas M ou F para sexo")
while True:
    try:
        idade = int(input("Informe sua idade: "))
    except ValueError:
        print("Digite a idade correta e tente novamente")
    else:
        if idade != 0: 
            print(f"Seja bem-vindo, {nome}") # como só fazer rodar números acima de zero? (try?)
            break
        else:
           print("Idade não ser menor ou igual a zero")
     
           
