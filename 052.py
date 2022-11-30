n=int(input('numero '))
t=0
for c in range(1, n +1):
    if n % c==0:
        print('\33[33m', end=' ')
        t += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n \33[m numero {} foi divisivel {} vezes'.format(n, t))
if t==2:
    print('por isso ele e primo')
else:
    print('por isso nao e primo')
