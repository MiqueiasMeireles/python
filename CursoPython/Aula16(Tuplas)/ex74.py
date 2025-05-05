from random import randint
números= (randint(1,10),randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram:')
for n in números:
  print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')
print('-'*30)

from random import sample
a= tuple(sample(range(1,10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')
