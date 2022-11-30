p=int(input('primeiro termo: '))
r=int(input('razao: '))
t=p
c=1
m=10
tot=0
while m != 0:
    tot=tot+m
    while c <=tot:
        print('{} >'.format(t), end=' ')
        t+=r
        c+=1
    print('pause..')
    m=int(input('qtos numeros vc quer? '))
print('finalizado com {}'.format(tot))
