from random import randint
from time import sleep
o=('pedra', 'papel', 'tesoura')
pc= randint (0, 2)
print('''suas opcoes
(1) pedra
(2) papel
(3) tesoura''')
j=int(input('qual sua jogada? '))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('po')
sleep(1)
print('-='*11)
print('o pc jogou {}'.format(o[pc]))
print('o jogador jogou {}'.format(o[j]))
print('-='*11)
if pc==0: #pedra
    if j==0:
        print('empate')
    elif j==1:
        print('jogador vence')
    elif j==2:
        print('pc vence')
    else:
        print('jogada invalida')

elif pc==1:#papel
    if j == 0:
        print('pc vence')
    elif j == 1:
        print('empate')
    elif j == 2:
        print('jogador vence')
    else:
        print('jogada invalida')
elif pc==2:#tesoura
    if j == 0:
        print('jogador vence')
    elif j == 1:
        print('pc vence')
    elif j == 2:
        print('empate')
    else:
        print('jogada invalida')
