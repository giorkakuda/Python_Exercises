#d=float(input('qual a distancia? '))
#if d<=200:
#    print('o valor da passagem sera R${:.2f}'.format(0.50 * d))
#else:
 #   print('o valor da viagem sera R${:.2f}'.format(0.45 * d))
print('-=-'*10)
d=float(input('qual a distancia? '))
if d<=200:
   p=0.50 * d
else:
   p=0.45 * d

print('o valor da passagem sera \33[4:32:40m R${:.2f}\33[m'.format(p))
