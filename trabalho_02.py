# Programa Temperaturas
temperaturas = [35,30,28,29,23,39,24,18,15]
print("Ordem Crescente")
temperaturas.sort()
print(temperaturas)
print("Menor temperaturaem Graus Celsius é:")
print(min(temperaturas))
print("Maior temperatura em Graus Celsius é:")
print(max(temperaturas))
print("A média das temperaturas em Graus Celsius é:")
media = sum(temperaturas) / len(temperaturas)
print(f"{media:.2f}")
