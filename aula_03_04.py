# Iguais ou Diferentes
n1 = int(input("Informe o número:"))
n2 = int(input("informe o número:"))
if n1 == n2:
    # produto = n1 * n2 (poderia incluir no print n1*n2 ao invés de criar uma váriavel igual abaixo, porém não está armazenado em lugar nenhum) *Serve para else
    produto = n1 * n2
    print(f"Os valores são iguais, portando o produto deles é {produto}.")
else:
    soma = n1 + n2
    print(f"Os valores são diferentes, portando a soma deles é {soma}.")
