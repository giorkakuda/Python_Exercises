n=c=soma=0
n=int(input('digite um n°(999 para parar) '))
while n != 999:
    soma += n
    c+=1
    n = int(input('digite um n°(999 para parar) '))
print('a qtd de numeros foi {} e a soma foi {}'.format(c, soma))
