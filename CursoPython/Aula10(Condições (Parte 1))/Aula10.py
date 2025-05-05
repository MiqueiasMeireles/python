n = str(input('Digite seu nome: ')).capitalize()
if n == 'Mique':
    print('Gostei desse nome')
print('Bom dia')

n1 = float(input('1° nota: '))
n2 = float(input('2° Nota: '))
m = (n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
if m>=5:
    print('Aluno aprovado.')
else:
    print('Aluno Reprovado\n Aguarde a prova de recuperação...')