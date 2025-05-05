from datetime import date
a = int(input('(Digite 0 para saber o atual) Ano: '))
if a==0:
    a = date.today().year
if a % 4 == 0 and a % 100!= 0 or a % 400 == 0:
    print(a,'é bissexto')
else:
    print(a,'não é bissexto')