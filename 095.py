time= list()
jogador=dict()
partida=list()
while True:
    jogador.clear()
    jogador['nome']=str(input('nome do jogador: '))
    tot=int(input(f'qtas partidas o {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0,tot):
        partida.append(int(input(f'qtos goals na partida {c+1}? ')))
    jogador['goals']= partida[:]
    jogador['total']= sum(partida)
    time.append(jogador.copy())
    while True:
        resp=str(input('continua(S/N)? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO, responda S ou N')
    if resp == 'N':
        break
print('=-'*30)

print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca=int(input('mostrar qual jogador? (999 parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO nao existe esse cod.')
    else:
        print(f'   Jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["goals"]):
            print(f'no jogo {i+1} fez {g} goals')
print('-='*40)
