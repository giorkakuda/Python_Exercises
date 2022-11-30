from math import radians, sin, cos, tan
a=float(input('angulo'))
s= sin (radians(a))
print('o angulo {} seno é {:.2f}'.format(a, s))
c= cos(radians(a))
print('o angulo {} coseno é {:.2f}'.format(a, c))
t= tan(radians(a))
print('o angulo {} tangente é {:.2f}'.format(a, t))
