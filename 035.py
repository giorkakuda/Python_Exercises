a=float(input('seguimento a: '))
b=float(input('seguimento b: '))
c=float(input('seguimento c: '))
if a < b + c and b < a + c and c < a + b:
    print('os seguimentos acima podem formar um triangulo')
else:
    print('os seguimento nao podem formar um triangulo')
