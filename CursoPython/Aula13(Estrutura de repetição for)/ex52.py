n = int(input('Número: '))
total = 0
for c in range(1,n +1):
    if n % c == 0:
        print('\033[32m',end='')
        total += 1
    else:
      print('\033[31m',end='')
    print('{} '.format(c), end='')
print('\033[m\nO número {} foi divisível {} vezes'.format(n,total))
if total ==2:
    print('Logo É PRIMO')
else:
    print('Logo NÃO É PRIMO')