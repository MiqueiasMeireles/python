n1 = float(input('1° segmento: '))
n2 = float(input('2° segmento: '))
n3 = float(input('3° segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
  print('Os segmentos PODEM FORMAR um triângulo', end=' ')
  if n1 == n2 == n3: #poderia fazer n1 == n2 and n2 == n3, mas o python permite fazer direto
    print('EQUILÁTERO')
  elif n1 != n2 != n3 != n1: #mesmo exemplo de cima,pode fazer direto
    print('ESCALENO')
  else:
    print('ISOCELES')
else:
  print('Não podem formar um triângulo ')
