# Programa Velidade Média
CM = 12 
DP = float(input("Distância Percorrida(KM):"))
Tempo = float(input("Tempo de Viagem(HORA):"))
VM = DP/Tempo
L = DP / CM
print (f"A velocidade média do veículo foi {VM} km/h.")
print (f"A quantidade gasta de combustível foi {L:.1f} litros.")