#Se as variáveis tiverem o mesmo valor, pode atribuí-las em uma única linha: n = qntn = s = 0
n = 0
qntn = 0 #quantidade de números
s = 0
while True:
    n = int(input('Digite um númeero [999 para parar]: '))
    if n == 999:
        break
    qntn += 1
    s += n
print(f'Dos {qntn números digitados, o resultado foi {s}.')