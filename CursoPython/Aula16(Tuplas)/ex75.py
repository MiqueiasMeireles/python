from operator import index
from os.path import split
n = (int(input('1° Número:')),
    int(input('2° Número:')),
    int(input('3° Número:')),
    int(input('4° Número:')))
print('-'*10)
print(f'O número 9 foi encontado {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro número 3 está na {n.index(3)+1}° posição')
else:
    print('Você não digitou o valor 3')
print('Os valores pares foram ' , end='')
for n in n:
    if n % 2 == 0:
        print(n,end=' ')
