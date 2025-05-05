from random import randint
from time import sleep
print('Vamos jogar!')
print('JO')
sleep(1)
print ('KEN')
sleep (1)
print('PO!!!')
print('[0]PEDRA\n[1]PAPEL\n[2]TESOURA')
lista = ('PEDRA','PAPEL','TESOURA')
pc = randint(0, 2)

j = int(input('jogada: '))
print('-=' * 11)
print('COMPUTADOR JOGOU {}'.format(lista[pc]))
print('JOGADOR JOGOU {}'.format(lista[j]))
print ('-=' * 10)
if j > 2:
  print('Jogada inválida')
  print('Empate')
elif pc == 1 and j == 0 or pc == 2 and j == 1 or pc == 0 and j == 2:
  print('Você perdeu')
else:
    print('Você venceu!')