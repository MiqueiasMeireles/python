s = float(input('Salário atual : '))
if s > 1250:
    se = s + (s * 10 / 100)
    print('De R${} passará a receber R${}'.format(s,se))
else:
    se = s + (s * 15 / 100)
    print('De R${:.2f} passará a receber R${:.2f}'.format(s,se))