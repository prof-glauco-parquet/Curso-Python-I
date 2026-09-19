# converter moedas REAL / DÓLAR / EURO
from os import system
system('cls')

celsius = float(input('Digite a temperatura em Celsius: '))

print('Escolha a temperatura para conversão: ')
print('1 - Fahrenheit')
print('2 - Kelvin')
opcao = int(input('Opção: '))

if opcao == 1:
    fahrenheit = celsius * 1.8 + 32
    print('{:.2f}°C equivale a {:.2f}ºF' . format(celsius, fahrenheit))
elif opcao == 2:
    kelvin = celsius + 273.15
    print('{:.2f}°C equivale a {:.2f}K' . format(celsius, kelvin))
else:
    print('Opção inválida!')