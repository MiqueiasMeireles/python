print('{:=^40}'.format(' LOJAS GUANABARA '))
pn = float(input('Preço: '))
op = int((input('Opção: ')))
if op == 1:
    t = pn - (pn * 0.10)
    print(t)
elif op == 2:
    t = pn - (pn * 0.05)
elif op == 3:
    t = pn
    pc = t / 2
    print(pc)
elif op == 4:
    t = pn + (pn * 0.20)
    tp = int(input('Quantas parcelas?'))
    p = t/ tp
    print(p)
