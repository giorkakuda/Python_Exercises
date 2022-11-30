s1=float(input('a: '))
s2= float(input('b: '))
s3=float(input('c: '))
if s1<s2+s3 and s2<s1+s3 and s3<s2+s1:
    print('podem formar um triangulo')
    if s1 == s2 == s3:
        print('equilatero')
    elif s1 != s2 != s3 != s1:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('nao podem formar um triangulo')
