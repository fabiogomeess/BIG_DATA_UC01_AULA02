# Programa para somar dois valores através de uma função
def somar(num1,num2): # função
    soma = num1 + num2
    print(f"A soma dos valores é {soma}")
def subtrair(num1,num2):
    sub = num1 - num2
    print(f"A soma dos valores é {sub}")
n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
somar(n1,n2)
subtrair(n1,n2) #encapsulamento - função dentro da outra