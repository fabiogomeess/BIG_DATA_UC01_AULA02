# Programa que armazena e lista os dados de um vetor
nomes = [] #primeiro acontece a declaração da lista para que o input seja usado e consigamos preencher os dados requeridos e armazena-los na lista
idades = [] 
#Coletando os dados
for i in range(5):
    nomes.append(input("Informe o nome: ")) # append é do comando para armazenar dados dentro do vetor(lista)
    idades.append(int(input("Informe a idade: ")))
print("Listagem dos usuários")
# Listando os dados
for i in range(len(nomes)):
     print(f"{nomes[i]} - {idades[i]}")
