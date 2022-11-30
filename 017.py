'''o=float(input('cateto oposto'))
a=float(input('cateto adjacente'))
h= (o ** 2 + a ** 2) ** (1/2)
print('o valor da hipotenusa é {:.2f}'.format(h))

*h= (1/2) foi ensinado na aula 07 como calcular a raiz do numero'''

from math import hypot
o=float(input('cateto oposto'))
a=float(input('cateto adjacente'))

print('o valor na hipotenusa é {}'.format(hypot(o, a)))
