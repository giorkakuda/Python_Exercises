numeros=[]
while True:
    n=int(input('digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('adicionado')
    else:
        print('duplicado')

    r=str(input('continua?(S/N) ')).strip().upper()
    if r in 'Nn':
        break
numeros.sort()
print(f'numero digitados: {numeros}')

