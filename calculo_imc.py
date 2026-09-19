from os import system
system('cls')

# Calculadora de IMC
# Pede para usuário digitar a altura
altura = input('Digite a sua altura em metros: ')
# Substitui vírgula por ponto e converte em decimal
altura = float(altura.replace(',' , '.'))
# Pede para usuário digitar o peso, 
# substitui vírgula por ponto e converte em decimal
peso = float(input('Digite o seu peso em Kg: ').replace(',' , '.'))

# imc = peso / (altura * altura)
imc = peso / (altura ** 2)

# print('Seu IMC: {}' . format(imc))
print(f'Seu IMC: {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está com o peso ideal')
elif imc < 30:
    print('Excesso de peso')
elif imc < 35:
    print('Obesidade grau I')
elif imc < 40:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')