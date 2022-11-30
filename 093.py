jogador=dict()
partidas=list()
jogador['nome']=str(input('nome do jogador: '))
tot=int(input('total de partidas: '))
for c in range(0,tot):
    partidas.append(int(input(f'    qtos goal na partida {c+1}? ')))
jogador['goals']=partidas[:]
jogador['total']=sum(partidas)
print('=-'*30)
print(jogador)
for k,v in jogador.items():
    print(f'- o campo {k} tem o valor de {v}')
print('-=' * 30)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["goals"])} partidas')
for i,v in enumerate(jogador['goals']):
    print(f'na partida {i+1} fez {v} goals')
