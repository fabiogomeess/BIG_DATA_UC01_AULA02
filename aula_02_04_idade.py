# Programa Idade
import datetime # importa a biblioteca datetime
data_atual = datetime.date.today() # armazena a data completa
nasc = int(input ("Qual é o ano do seu nascimento?"))
ano_atual = data_atual.year # armazena na variavel o ano atual
idade = ano_atual - nasc
print (f"De acordo com seu ano de nascimento, a sua idade é de {idade} anos.")