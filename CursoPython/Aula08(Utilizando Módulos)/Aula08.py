import math
n = int(input('Exemplo 1'))
raiz = math.sqrt(n)
print('A raiz de {} é {}'.format(n,math.ceil(raiz)))
# import importa tudo da biblioteca específica, já from import só o que você quer. ceil arredonda para cima, floor arredonda para baixo

from math import sqrt, floor
n = int(input('Exemplo 2'))
raiz = sqrt(n)
print('A raiz de {} é {:.2f}'.format(n,floor(raiz)))