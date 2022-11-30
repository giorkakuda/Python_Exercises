c=s=0
while True:
    n=int(input('digite um n°(999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'a qtd de n° foi {c} e soma foi {s}')
