s=str(input('digite o sexo(M/F): ')).strip().upper()[0]
while s not in 'MmFf':
    s=str(input('valor invalido para {} tente novamente'.format(s))).strip().upper()[0]
print('sexo {} registrado'.format(s))
