#Se as variáveis tiverem o mesmo valor, pode atribuí-las em uma única linha: n = qntn = s = 0
n = 0
qntn = 0 #quantidade de números
s = 0
while n != 999:
    n = int(input('Digite um númeero [999 para parar]: '))
    qntn += 1
    s += n
print('Dos {} números digitados, o resultado foi {}.'.format(qntn-1 ,s-999))