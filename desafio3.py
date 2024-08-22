# Declaração de variável e conversão dos valores
metro = float(input("Digite a quantidade de metros: "))
centimetro = metro*100
milimetro = metro*1000
quilometro = metro/100

# Impressão dos valores convertidos
print(f'O seu valor de metros em centimetros é: {centimetro:.2f}, O seu valor de metros em milimetros é: {milimetro:.2f}, O seu valor de metros em quilometros é: {quilometro:.2f}')

