frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' #Pode utilizar um macete do fateamento. junto [::-1] assim ele mostraria a frase de trás para frente
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto,inverso ))
if inverso == junto:
    print('Palíndromo')
else:
    print('Não é um palíndromo')