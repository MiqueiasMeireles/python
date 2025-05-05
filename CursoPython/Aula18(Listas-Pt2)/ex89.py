aluno = []
while True:
    n = str(input('Nome: ')).capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    e = input('Continuar? ')
    aluno.append([n, [n1,n2], m])
    if e in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i,a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
print('-' * 26)
while True:
    e2 = int(input('Deseja mostrar as notas de qual aluno? [999break]:'))
    if e2 == 999:
        break
    if e2 <= len(aluno) - 1:
        print(f'Notas de {aluno[e2][0]} são {aluno[e2][1]}')

