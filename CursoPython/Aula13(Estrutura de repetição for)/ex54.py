from datetime import date
aa = date.today().year
maior = 0
menor = 0
for c in range(1,5):
    an = int(input('Ano de Nascimento da {}° pessoa : '.format(c)))
    i = aa - an
    if i >=21:
        maior += 1
    else:
        menor +=1
print('{} maior(es) de idade\n{} menor(es) de idade'.format(maior, menor))
