# Declaração de variável e conversão dos valores
temp_celsius = float(input("Digite a temperatura em celsius: "))
temp_fahr = (temp_celsius*9/5)+32
temp_kelvin = temp_celsius+273.15

# Impressão dos valores digitados e convertidos
print(f'A temperatura em celsius é: {temp_celsius:.2f}, convertida para Fahrenheit é: {temp_fahr:.2f}, e convertida para kelvin é: {temp_kelvin:.2f}')
