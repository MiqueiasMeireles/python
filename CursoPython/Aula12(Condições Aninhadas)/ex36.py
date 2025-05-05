v = float(input('Digite o valor da casa: '))
s = float(input('Qual o seu salário? '))
t = int(input('Em quantos anos planeja pagar?' ))
pm =  v // (12 * t)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(v,t,pm))
#pode fazer outra print na linha abaixo para continuar a linha de cima. para isso no depois do .format() digite: , end=' ')
if pm >= s * 0.30:
    print('\033[31mNegado')
else:
    print('\033[32mAprovado!')