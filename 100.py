from random import randint

def sorteia(lista):
    print('os numeros sorteados sao: ', end=' ')
    for cont in range(0,5):
        r=randint(1,10)
        lista.append(r)
        print(r, end=' ')


def somapar(lista):
    soma=0
    for valor in lista:
        if valor % 2==0:
            soma += valor
    print(f'somando os pares de {lista}, temos {soma}')

numeros=list()
sorteia(numeros)
somapar(numeros)