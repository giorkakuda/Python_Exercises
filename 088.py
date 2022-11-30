from random import randint
from time import sleep
lista=list()
jogos=list()
print('=='*25)
print('                Jogo da Mega')
print('=='*25)
q=int(input('qtos jogos? '))
tot=1
while tot <= q:
    cont = 0
    while True:
        n=randint(0,60)
        if n not in lista:
            lista.append(n)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print(f'sorteando {q} jogos')
sleep(1)
for i, l in enumerate(jogos):
    print(f'{i+1}: {l}')