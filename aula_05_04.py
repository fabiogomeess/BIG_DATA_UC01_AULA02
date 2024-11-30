# Programa para determinar a quantidade de valores pares e ímpares
qnt_par = 0
qnt_impar = 0
numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        qnt_par +=1
    else:
        qnt_impar += 1 
print(f"A quantidade de números pares é: {qnt_par}")
print(f"A quantidade de números impares é: {qnt_impar}")
print("Ordem de Criação")
print(numeros)
print("Ordem Reversa")
numeros.reverse()
print(numeros)
print("Ordem Crescente")
numeros.sort()
print(numeros)
