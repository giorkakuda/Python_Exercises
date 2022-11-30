classe= 'arcondicionado'
modelo= '1200'
carga= 'eletrica'
liga = 'logico'


while True:
    n = int(input('Bem vindo, digite 1 - para gelar, 2- para desligar: '))
    if n==1:
        print('gelando...')

    elif n==2:
        print('equipamento desligado, aperte 1 para ligar ou 3 para sair')
    elif n==3:
        print('obrigado volte sempre!!')
        break
    else:
        print('opcao invalida tente novamente')


