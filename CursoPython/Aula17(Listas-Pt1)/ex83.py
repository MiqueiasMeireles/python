expr = input('Digite a expressão: ')
lista = []
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão Válida')
else:
    print('Expressão Inválida')