lista=[]

for c in range(0,5):
    n=int(input('digite numero: '))
    if c == 0 or n> lista[-1]:
        lista.append(n)
    else:
        pos=0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos += 1
print(f'os valores digitados na ordem {lista}')

