ma=me=q=s=m=0
r='s'
while r in 'Ss':
    n=int(input('numero: '))
    s+=n
    q+=1
    if q==1:
        ma=me=n
    else:
        if n>ma:
            ma=n
        if n<me:
            me=n
    r=str(input('deseja continuar?(S/N) ')).strip().upper()[0]
m=s/q
print('digitou {} e a media dos valores e {}, '.format(q, m))
print('o maior e {} e o menor e {}'.format(ma, me))
