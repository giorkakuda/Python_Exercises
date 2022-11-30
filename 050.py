soma=0
cont=0
for c in range(1, 7):
    n = int(input('digite numero {} valor: '.format(c)))
    if n % 2==0:
        soma=soma+n
        cont=cont+1
print('informou {} pares e a soma e {}'.format(cont, soma))


