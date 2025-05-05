n1 = int(input('1° número: '))
n2 = int(input('2° número: '))
n3 = int(input('3° número: '))
me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n2:
    me = n3
print('O menor número é:',me)
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
print('O maior número é',ma)