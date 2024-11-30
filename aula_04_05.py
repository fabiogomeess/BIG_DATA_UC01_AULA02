# Programa média e a situação dos alunos 
for i in range(3):
    nome = input("Informe o nome do estudante: ")
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    media = (nota1 + nota2) / 2
    if media >= 10:
        print(f"{nome}, você está APROVADO.")
    elif media >= 3:
        print(f"{nome}, você está em RECUPERAÇÃO")
    else:
        print(f"{nome}, você está REPROVADO")
