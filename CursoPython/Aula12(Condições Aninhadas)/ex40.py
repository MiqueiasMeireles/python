n1 = float(input('1°Nota: '))
n2 = float(input('2°Nota: '))
m = (n1 + n2) / 2
print('A média entre {} e {} é {}'.format(n1,n2,m))
if m >= 7.0:
  print('Aprovado!')
elif m >= 5.0:
  print('Recuperação')
elif m < 5:
  print("Reprovado")


