from os import system
system('cls')
import time

# Inicia contagem do "multiplicando"
for i in range(1,11):
    print(f'Tabuada do {i}')
    # Inicia contagem do "multiplicador"
    for ii in range(1,11):
        # Monta a expressão de multiplicação - Ex: 1 x 1 = 1
        print(f'{i} x {ii} = {i*ii}')
        time.sleep(0.5)
    print('')