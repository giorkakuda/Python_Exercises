n= (int(input('valor: ')),
    int(input('valor: ')),
    int(input('valor: ')),
    int(input('valor: ')))

print(f'o valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'o valor 3 apareceu na posicao {n.index(3)+1}')
else:
    print('o 3 nao foi digitado')
print('os numeros pares foram', )
for c in n:
    if c % 2 ==0:
        print(c)
