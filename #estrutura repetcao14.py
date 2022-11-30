'''for c in range(1, 10):
    print(c)
print('fim')'''

'''c=1
while c < 10:
    print(c)
    c=c+1
print('fim')'''

#n=1
#while n != 0:
 #   n=int(input('valor: '))
#print('fim..')

'''r='S'
while r=='S':
    n=int(input('valor: '))
    r=str(input('continua? ')).upper()
print('fim')'''

n=1
par=impar=0
while n != 0:
    n=int(input('valor: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar+=1
print('vc digitou {} impares e {} pares'.format(impar, par))


