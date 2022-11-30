lista=[]
par=[]
impar=[]

while True:
    lista.append(int(input('digite numero: ')))
    r=str(input('continua? ')).strip().upper()
    if r in 'Nn':
        break
for i,v in enumerate(lista):
    if v % 2==0:
        par.append(v)
    else:
        impar.append(v)

print(f'os numeros digitados foram {lista} ')
print(f'os numeros impares foram {impar}')
print(f'os numeros pares foram {par}')
