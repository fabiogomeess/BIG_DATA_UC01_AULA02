# PROGRAMA USANDO LISTA COM OPERADORES MATEMÁTICOS (MAX, MIN, SUM E USANDO TÉCNICAS DO LEN PARA DIVISÃO, % e **(calcula potencia))
num = [10,20,12,30,100,90,25,5,45,60] #Praticando 1
num_01 = []
print(f"A soma dos valores é {sum(num)}.")
print(f"O maior valor é {max(num)} e o menor valor é {min(num)}.")
print(f"A média dos valores é {sum(num) / len(num)}") # len define a quantidade de elementos numa lista (ex.: na lista "num", temos 10 elementos e o len conta um por um.)
num_01 = num.sort() # para colocar em ordem crescente 
print(num_01)