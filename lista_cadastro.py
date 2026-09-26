from os import system
system('cls')

clientes = []
telefones = []

opcao = ''

while opcao.upper() != 'X':
    system('cls')
    nome = input('Digite o nome do cliente: ')
    telefone = input('Digite o telefone do cliente: ')

    clientes.append(nome)
    telefones.append(telefone)

    system('cls')
    print('-- CADASTRO REALIZADO COM SUCESSO --')

    opcao = input('Aperte X para Finalizar ou Enter para continuar: ')

# Limpa a tela
system('cls')
# Listar registros -> Nome: Glauco - Telefone: 123456789
for i in range(len(clientes)):
    print(f'Nome: {clientes[i]} - Telefone: {telefones[i]}')

