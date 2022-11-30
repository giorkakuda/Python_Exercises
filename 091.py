from random import randint
from operator import itemgetter
from time import sleep
jogo={'jogador 1': randint(1,6),
      'jogador 2': randint(1,6),
      'jogador 3': randint(1,6),
      'jogador 4': randint(1,6)}
ranking=list()
for k, v in jogo.items():
      print(f'jogador {k} tirou {v} no dado')
      sleep(1)
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-'*20)
print('  == Ranking ==')
for i, v in enumerate(ranking):
      print(f'{i+1}° lugar {v[0]} com {v[1]}')
      sleep(1)