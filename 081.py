lista= []
while True:
    lista.append(int(input('numero: ')))
    r=str(input('continua? (S/N): '))
    if r in 'Nn':
       break

lista.sort(reverse=True)
print(f'vc digitou {len(lista)} numeros')
print(f'os numeros na ordem decrescente sao {lista}')
if 5 not in lista:
    print('o 5 nao foi digitado')
else:
    print('o cinco foi digitado')
