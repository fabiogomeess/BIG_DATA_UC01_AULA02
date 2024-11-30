# Programa Contracheque
valor_hora = int(input("Informe o valor da hora do funcionário: "))
horas_trabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
salario_bruto = valor_hora * horas_trabalhadas
imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salário_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)
print(f"Seu salário bruto é R$ {salario_bruto:.2f}")
print(f"Desconto IRRF: R$ {imposto_de_renda:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto Sindicato: R$ {sindicato:.2f}")
print(f"Com todos os descontos obrigatórios, seu salário líquido ficou em R$ {salário_liquido:.2f}.")