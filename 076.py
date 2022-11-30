print(f'{"Lista de precos":^40}')
print('-='*20)
l= ('lapis', 1.99,
    'borracha', 1.30,
    'caderno', 16.90,
    'mochila', 168.99,
    'estojo', 20.00,
    'caneta', 5.00,
    'livro', 200.00)
for pos in range(0, len(l)):
    if pos % 2==0:
        print(f'{l[pos]:.<30}', end='')
    else:
        print(f'R${l[pos]:>7.2f} ')
