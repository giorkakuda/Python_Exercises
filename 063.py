fib=int(input('qto numeros da seq.? '))
f1=0
f2=1
print('seq. {} > {}'.format(f1, f2),end=' ')
cont=3
while cont <=fib:
    f3=f1+f2
    print('<{}'.format(f3), end=' ')
    f1=f2
    f2=f3
    cont+=1


