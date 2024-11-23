# boletim
nome = input("Informe o nome do estudante:")
N1 = float(input("informe a nota:"))
N2 = float(input("Informe a nota:"))
média = (N1+N2) / 2
print (f"A nota para passar direto é 7, sua média é {média}.")
if média >= 7: 
    print(f"Parabéns, {nome}. Você foi aprovado!")
elif média >= 3:
    print(f"{nome}, infelizmente você está de recuperação")
else:
    print(f"{nome}, infelizmente você está reprovado")