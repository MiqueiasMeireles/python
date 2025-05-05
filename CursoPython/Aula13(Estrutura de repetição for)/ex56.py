somai = 0
media = 0
homemimaior = 0
nomevelho = ''
totmulher20 = 0
for pessoas in range(1,5):
  print ('---- {}° Pessoa ----'.format(pessoas))
  n = str(input('Nome: ')).strip()
  i = int(input('Idade: '))
  s = str(input('Sexo (M/F): ')).strip()
  somai += i
  media = somai / 4
  if pessoas == 1 and s in 'Mm':
    homemimaior = i
    nomevelho = n
  if s in 'Mm' and i > homemimaior:
    homemimaior = i
    nomevelho = n
  if s in 'Ff' and i < 20:
    totmulher20 += 1
print('A média das idades é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(homemimaior,nomevelho))
print ('Ao todo são {} mulher(es)) com menos de 20 anos'.format(totmulher20))
