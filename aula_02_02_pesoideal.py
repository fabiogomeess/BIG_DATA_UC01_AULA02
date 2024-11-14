#Programa Peso Ideal?
altura = float(input("Qual a sua altura?(metros)"))
homens = (72.7*altura) - 58
mulheres = (62.1*altura) - 44.7
print(f"O seu peso ideal, de acordo com a sua altura e seu sexo (h), é de {homens:.2f}kgs")
print(f"O seu peso ideal, de acordo com a sua altura e seuu sexo (m), é de {mulheres:.2f}kgs")

