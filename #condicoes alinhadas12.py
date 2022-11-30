n=str(input('Qual seu nome? ')).strip().lower()
if n==('giordanni'):
    print('\33[1:32:40m Que nome bonito!!!\33[m')
elif n=='maria' or n== 'lucia' or n== 'ana':
    print('é um nome feminino bem comum')
elif n in 'paula priscila juliana':
    print('seu nome e popular')
else:
    print('seu nome é comum')
