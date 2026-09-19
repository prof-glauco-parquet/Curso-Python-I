from os import system
system('cls')

nomes = []
total = int(input("Quando nomes deseja cadastrar? "))
system('cls')

for i in range(0,total):
    nomes.append(input('Digite um nome: '))
    system('cls')

for i in range(0,total):
    print(f'{i} - {nomes[i]}')


