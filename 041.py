from datetime import date
y=date.today().year
n=int(input('nascimento: '))
a= y - n
print('sua idade e de {} anos e vc esta na categoria'.format(a))
if a<=9:
    print('Mirim')
elif a<=14:
    print('Infantil')
elif a<=19:
    print('Junior')
elif a<=25:
    print('Senior')
elif a>25:
    print('Master')
