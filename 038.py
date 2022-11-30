n1=int(input('primeiro: '))
n2=int(input('segundo: '))
if n1>n2:
    print('o numero \33[1:31:40m {} \33[m é maior que o numero {}'.format(n1, n2))
elif n1<n2:
    print('o numero {} e menor que {}'.format(n1,n2))
else:
    print('os numeros sao iguais')
