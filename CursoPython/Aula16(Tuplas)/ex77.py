#for p in palavras: Significa (para cada palavra no conjunto palavras
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso')
for p in palavras:
    print(f'\nNa Palavra {p.upper()} temos: ', end = '')
    for letra in p:
        if letra.lower() in 'aeio':
            print(letra, end=' ')
