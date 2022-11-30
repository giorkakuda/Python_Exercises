lista=[]
galera=[]
ma=me=0
while True:
    lista.append(str(input('nome: ')))
    lista.append(float(input('peso: ')))
    if len(galera) == 0:
        ma=me=lista[1]
    else:
        if lista[1] > ma:
            ma=lista[1]
        if lista[1] < me:
            me=lista[1]
    r=str(input('continua?(S/N)? '))
    galera.append(lista[:])
    lista.clear()
    if r in 'Nn':
        break

print(f'o numero de pessoas cadastradas foram {len(galera)}')
print(f'o maior peso foi de {ma}kg peso de ', end='')
for p in galera:
    if p[1] == ma:
        print(f'[{p[0]}]', end='')
print(f'o menor peso foi de {me}. peso de ', end='')
for p in galera:
    if p[1] == me:
        print(f'[{p[0]}]', end='')