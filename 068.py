from random import randint
w=0
while True:
    j=int(input('numero: '))
    pc=randint(0,10)
    t = j + pc
    v=' '
    while v not in 'PI':
        v = str(input('par ou impar: ')).strip().upper()[0]
    print(f'{j} mais {pc} e igual a {t}')
    if v == 'P':
        if t %2==0:
            print('vc ganhou')
            w+=1
        else:
            print('vc perdeu')
            break
    elif v =='I':
        if t%2==1:
            print('vc ganhou')
            w+=1
        else:
            print('vc perdeu')
            break
print(f'vc ganhou {w} partidas')

