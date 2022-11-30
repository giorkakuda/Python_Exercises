n=int(input('numero: '))
print('''escolha uma das bases de conversao:
(1) converter para binario
(2) converter para octal
(3) converter para hexadecimal''')
o=int(input('escolha sua opcao: '))
if o==1:
    print('{} valor para binario e {}'.format(n, bin(n)))
elif o==2:
    print('{} valor convertido para octal e {}'.format(n,oct(n)))
elif o==3:
    print('{} valor para hexadecimal e {}'.format(n, hex(n)))
else:
    print('opcao invalida')
