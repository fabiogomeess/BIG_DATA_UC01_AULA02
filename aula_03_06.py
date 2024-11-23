# Qual o maior número
n1 = int(input("informe o número:"))
n2 = int(input("informe o número:"))
n3 = int(input("informe o número:"))
if n1>n2 and n1>n3:
    print("O primeiro número é o maior")
elif n2>n1 and n2>n3:
    print("O segundo número é o maior")
else:
    print("O terceiro número é o maior")