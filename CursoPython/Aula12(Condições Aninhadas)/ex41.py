from datetime import date
a = int(input('Ano de nascimento: '))
aa = date.today().year
i = aa-a
print('Sua idade é {} anos logo, sua categoria é'.format(i),end=' ')
if i <=9:
    print('Mirin')
elif i <=14:
    print ("Infantil")
elif i <=19:
    print ("júnior")
elif i <=25:
    print ("Sênior")
else:
    print ("Master")
