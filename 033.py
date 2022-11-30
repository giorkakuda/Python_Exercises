a = int(input('primeiro '))
b = int(input('segundo '))
c = int(input('terceiro '))
#menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior = c
print('o menor valor e {}'.format(menor))
print('o maior valor e {}'.format(maior))

