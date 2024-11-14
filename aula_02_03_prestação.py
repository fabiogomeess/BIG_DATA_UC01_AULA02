#Programa Prestação em Atraso
prestação = float(input("Qual valor da sua prestação?"))
tempo = float(input ("Quanto tempo em atraso(meses)?"))
taxa = float(input ("Qaul a taxa atual de juros?"))
valorfinal = (prestação+(prestação*(taxa/100)))*tempo
print (f"Considerando o tempo de atraso e juros ao decorrer desse tempo, o valor atual está em {valorfinal:.2f}")