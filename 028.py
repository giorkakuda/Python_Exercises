from random import randint
from time import sleep
print('>-<' * 13)
print('\033[1:31:40m vou pensar em um numero, tente advinhar...\33[m')
print('>-<' * 13)
n=int(input('Em qual numero pensei? '))
print('processando...')
sleep(3)
c= randint(1, 5)
if n==c:
    print('parabens, vc acertou!')
else:
    (print('Errou! haha'))
print('pensei no numero {}'.format(c))
