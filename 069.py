tot18=toth=totm=0
while True:
    i=int(input('idade: '))
    s=' '
    while s not in 'MF':
        s=str(input('sexo(M/F): ')).strip().upper()[0]
    if i >= 18:
            tot18 += 1
    elif s == 'M':
            toth += 1
    elif s=='F' and i < 20:
            totm += 1
    p=' '
    while p not in 'SN':
        p=str(input('continua?(s/n) ')).strip().upper()[0]
    if p == 'N':
            break
print(f'o n° de pessoas com mais de 18 anos e {tot18}')
print(f'o n° de homens foram {toth}')
print(f'o n° de mulheres com menos de 20 anos foram {totm}')
