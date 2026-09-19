from os import system
system('cls')
import time

# Inicia a contagem do "multiplicando"
for i in range(1,11):
    linha = ""
    # Limpa a variável "linha"
    for ii in range(1,11):
        # Vai armazenando toda a tabuada
        # ": >4" = totaliza 04 caracteres, completando com espaço vazio à esquerda
        linha += f'{i*ii: >4}' 
    # Mostra os resultados da tabuada do "multiplicando"
    print(linha)
    time.sleep(2)
