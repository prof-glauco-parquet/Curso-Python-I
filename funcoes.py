from os import system
system('cls')

def Somar(a,b):
    try:
        print(f'Soma: {a} + {b} = {a+b}')
    except:
        print('Erro desconhecido')
def Subtrair(a,b):
    try:
        print(f'Subtrair: {a} - {b} = {a-b}')
    except:
        print('Erro desconhecido')
def Multiplicar(a,b):
    try:
        print(f'Multiplicar: {a} x {b} = {a*b}')
    except:
        print('Erro desconhecido')
def Dividir(a,b):
    try:
        print(f'Dividir: {a} / {b} = {a/b}')
    except ZeroDivisionError as erro:
        print('Impossível divisão por ZERO')
    except:
        print('Erro desconhecido')

opcao = ''

while opcao.upper() != 'X':
    system('cls')
    num1 = float(input('Informe o primeiro número: '))
    num2 = float(input('Informe o segundo número: '))

    opcao = int(input(''' 
    Opções:
    [1] - Somar
    [2] - Subtrair
    [3] - Multiplicar
    [4] - Dividir
    Escolha uma opção acima: '''))

    if opcao == 1:
        Somar(num1, num2)
    elif opcao == 2:
        Subtrair(num1, num2)
    elif opcao == 3:
        Multiplicar(num1, num2)
    elif opcao == 4:
        Dividir(num1, num2)
    else:
        print('Opção inválida!')

    opcao = input('Aperte X para finalizar ou Enter para outro cálculo: ')