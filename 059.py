from time import sleep
v1=int(input('primeiro valor: '))
v2=int(input('segundo valor: '))
o=0
while o != 5:
    print('''voce gostaria de:
    (1) somar
    (2) multiplicar
    (3) maior
    (4) novos numeros
    (5) sair do programa''')

    o=int(input('>>>>>>>>>>opcao: '))
    if o==1:
        r1= v1+v2
        print('a soma dos numeros e {}'.format(r1))
    elif o==2:
        r2= v1*v2
        print('os numeros multiplicados sao {}'.format(r2))
    elif o==3:
        if v1>v2:
            print('{} e maior'.format(v1))
        elif v1<v2:
                print('{} e maior'.format(v2))
        else:
            print('os 2 sao iguais')
    elif o==4:
        v1 = int(input('primeiro valor: '))
        v2 = int(input('segundo valor: '))
    elif o==5:
        print('finalizando programa...')
    if o>5:
        print('opcao invalida')
    sleep(2)


