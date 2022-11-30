from datetime import date
atual= date.today().year
n=int(input('data de nascimento: '))
i= atual - n
print('quem nasceu em {} tem {} no ano de {}'.format(n, i, atual))

if i==18:
    saldo = i - 18
    print('vc tem que se alistar imediatamente'.format(saldo))
elif i<18:
    saldo = 18 - i
    print('ainda faltam {} para alistamento'.format(saldo))
elif i > 18:
    saldo = i - 18
    print('vc deveria ter se alistado {} anos atras'.format(saldo))
