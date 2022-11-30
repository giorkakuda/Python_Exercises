total=totmil=menor=cont=0
barato=''
while True:
    produto=str(input('Produto: ')).strip().upper()
    preco=float(input('Valor: R$ '))
    cont+=1
    total += preco
    if preco > 1000:
        totmil+=1
    if cont==1 or preco < menor:
        menor=preco
        barato = produto

    resp=' '
    while resp not in 'S/N':
        resp = str(input('deseja continuar?(S/N) ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o valor total e R${total}')
print(f'{totmil} produtos custam acima de R$1000,00')
print(f'o produto mais barato e {barato} que custa R${menor:.2f}')

