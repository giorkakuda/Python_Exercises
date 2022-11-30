from time import sleep
def contador(i, f, p):
    if p < 0:
        p*=-1
    if p == 0:
        p=1
    print(f'contagem de {i} a {f}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
    print('FIM')


#programa principal
contador(1,10,1)
contador(10,0,2)
print('Agora sua vez')
ini=int(input('Inicio: '))
fim=int(input('FIM: '))
pas=int(input('Passo: '))
contador(ini,fim,pas)
