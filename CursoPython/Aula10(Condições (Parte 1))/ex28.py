from random import randint
from time import sleep
cpu = randint(0,5)
j1 = int(input('Descubra o número: '))
print('processando'.upper())
sleep(1.07)
if cpu==j1:
    print('Parabéns você acertou!')
else:
    print('Você errou, eu pensei em {} Tente novamente!'.format(cpu))
