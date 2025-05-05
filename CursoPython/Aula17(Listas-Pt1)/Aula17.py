n = [2,5,9,1]
n[2] = 3
n.append(7)
n.sort(reverse = True)
n.insert(2,0) #esse comando adiciona um objeto a posição indicada
n.pop(4)
n.remove(3)
print(n)
print(f'Essa lista tem {len(n)} elementos')
for cont in range(0,2):
    n.append(int(input('Gigite um número: ')))
for pos,n in enumerate(n):
    print(f'Na posição {pos} eu encontrei o número {n}')

a = [2,3,4,5,7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')