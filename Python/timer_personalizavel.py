import os
from time import sleep

def timer(tempo):

    for i in range(tempo, 0, -1):
        print('\n','='*50,'\n')
        print(' Timer acabando em {} segundos'.format(i))
        print('\n','='*50,'\n')
        sleep(1)
        os.system('cls')


os.system('cls') # Opcional
timer(5)         # Coloque aqui o tempo desejado
print('Acabou!') # Opcional
