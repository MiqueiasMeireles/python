n = int(input('Digite um número: '))
print('''Escolha as opções de conversão.
[1]BINÁRIO
[2]OCTETO
[3]HEXADECIMAL''')
o = int(input('Opção: '))
if o == 1:
  print('Opção binário selecionada,o resultado é {} '.format(bin(n) [2:])) #utiliza o [2:] como faturamento da string (Aula09), retirando caracteres indesejados
elif o == 2:
  print('Opção octeto escolhida,o resultado é {}'.format(oct(n) [2:]))
elif o == 3:
    print('Opção hexadecimal escolhida,o resultado é {}'.format(hex(n) [2:]))
else:
      print('Opção inválida!')