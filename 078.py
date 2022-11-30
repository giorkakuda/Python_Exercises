valores=[]
ma=me=0
for c in range(0,5):
    valores.append(int(input(f'digite um valor para posicao {c}: ')))
    if c==0:
        ma=me=valores[c]
    else:
        if valores[c] > ma:
            ma=valores[c]
        if valores[c] < me:
            me=valores[c]
print(f'valores digitados {valores}')
print(f'o maior numero foi {ma} nas posicoes', end='')
for i, v in enumerate(valores):
    if v == ma:
        print(f'{i}...', )
print(f'o menor numero foi {me} nas posicoes', end='')
for i, v in enumerate(valores):
    if v==me:
        print(f'{i}...',)
