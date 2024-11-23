# Doação de sangue
idade = int(input("Informe a sua idade:"))
peso = int (input("Informe seu peso (kg):"))
sono = int(input("Informe quanto tempo dormiu nas últimas 24h:"))
if (16 <= idade <= 69) and (peso >= 50) and (sono >= 6):
    print("Você está apto para doar sangue, agora é só aguardar a sua vez.")
else:
    print("Infelizmente você não poderá doar seu sangue, mas agradecemos sua iniciativa. Você pode procurar um de nossos balcões de atendimento para saber mais")
    