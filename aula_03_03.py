#
nome = input("Informe seu nome:")
sexo = input("Informe seu sexo:")
idade = int(input("Infomre sua idade:"))
if (idade >= 18) and (sexo == "M" or sexo == "m"):
    certificado = int(input("Informe o certificado de reservista:"))
elif idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")