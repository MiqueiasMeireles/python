import math
a = float(input('Digite um Ângulo: '))
co = math.cos(math.radians(a))
sen = math.sin(math.radians(a))
tan = math.tan(math.radians(a))
print('Cosseno {:.3f}, Seno {:.3f} e Tangente {:.3f}'.format(co, sen, tan))