matriz=[[0,0,0],[0,0,0,],[0,0,0]]
par=mai=col=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'valor [{l}, {c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz [l][c] % 2 ==0:
            par+=matriz [l][c]
    print()
print(f'a soma dos pares e {par}')
for l in range(0,3):
    col+=matriz[l][2]
print(f'a soma da terceira coluna e {col}')
for l in range(0,3):
    if c==0:
        mai=matriz[1][c]
    elif matriz[1][c] >mai:
        mai=matriz[1][c]
print(f'o maior valor da segunda linha e {mai}')