from datetime import date
a = int(input('Ano de Nascimento: '))
aa = date.today().year
i = aa - a
print('Você nasceu em {} tem {} anos em {}'.format(a,i,aa))
if i < 18:
    t = 18 - i
    t2 = 18 + a
    print('Faltam {} ano(s) para o seu alistamento'.format(t))
    print('Seu alistamento será em {}'.format(t2))
elif i > 18:
    t = i - 18
    t2 = 18 + a
    print('Você deveria ter se alistado a {} ano(s)'.format(t))
    print('Seu alistamento foi em {}'.format(t2))
if i == 18:
    print('Você deve se alistar \033[7;97mIMEDIATAMENTE!\033[m')
