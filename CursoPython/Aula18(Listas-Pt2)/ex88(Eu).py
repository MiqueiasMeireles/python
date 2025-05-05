from random import sample
from time import sleep
cont = 0
print('='*30)
print('JOGO DA MEGA SENA'.center(30))
print('='*30)
n = int(input('Quantos jogos quer sortear? '))
print('-=' * 3, f'SORTEANDO {n} JOGOS', '-=' * 4)
while True:
    cont += 1
    a = tuple(sample(range(1, 61), 6))
    sleep(1)
    print(f'Jogo {cont}: {a}')
    sleep(1)
    if cont == n:
        break
print('-=' * 4, '< BOA SORTE! >', '-=' * 5)