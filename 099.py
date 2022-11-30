from time import sleep
def maior(*num):
    cont=maior=0
    print('analizando os valores...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior=valor
        else:
            if valor > maior:
                maior=valor
        cont +=1
    print(f'foram informados {cont} valores no total')
    print(f'o maior valor e {maior}')

#programa principal
maior(3,4,2,5,8,1)
maior(9,2,8)
maior(1,4)
