# PROGRAMA QUE MOSTRA O USO DE LISTAS
nomes_01 = "Alessandro, Maria, Eduarda"
nomes_02 = ["Alessandro", "Maria", "Eduarda"]
print(nomes_01)
print(nomes_02)
print(nomes_02[1])
print(len(nomes_02)) # o comando len determina a quantidade de registro numa lista/tabela 
print("Listagem dos elementos do Vetor")
n = 1
for i in range(len(nomes_02)):
    print(f"{n}º - {nomes_02[i]}") # O CÓDIGO ALT167 RESULTA NO -> º 
    n += 1 # essa formula serve sempre pra somar mais 1, incremento. 