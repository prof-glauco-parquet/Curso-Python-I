from os import system
system('cls')

# Funções para trabalhar com textos
nomecompleto = input('Digite seu nome completo: ')

# len = length - conta o número de caracteres
print('- Função para contar caracteres: ', len(nomecompleto))
# upper = transforma texto em maiúsculo
print('- Função para texto maiúsculo: ', nomecompleto.upper())
# lower = transforma texto em minúsculo
print('- Função para texto minúsculo: ', nomecompleto.lower())
# capitalize = transforma a primeira letra em maiúsculo
print('- Função para primeiro maiúsculo: ', nomecompleto.capitalize())
# title = transforma a primeira letra de cada palavra em maiúsculo
print('- Função para primeira letra de cada palavra maiúscula: ', nomecompleto.title())
# strip = remove espaços em branco antes e depois do texto
print('- Função para remover espaços antes e depois do texto: ', nomecompleto.strip())
# find = encontra a posição do caractere
espaco = nomecompleto.find(' ')
print('- Primeiro nome: ', nomecompleto[0:espaco])
# replace = busca e substitui texto
print('- Remover espaços vazios: ', nomecompleto.replace(' ', ''))
print('- Contar letras sem espaços: ' , len(nomecompleto.replace(' ', '')))