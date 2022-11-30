s=float(input('salario '))
if s <= 1250:
    n= s + (s * 15 / 100)
    print('o novo salario sera R${:.2f}'.format(n))
else:
    n= s + (s * 10 / 100)
    print(' o novo salario sera R${:.2f}'.format(n))
print(' \33[1:32:40m PARABENS PELO AUMENTO \33[m')

#11 CORES:  \33[1:32:40m     \33[m