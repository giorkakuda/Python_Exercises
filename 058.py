from random import randint
pc=randint(0,10)
print('vou pensar em um numero entre [0 e 10], consegue advinhar?')
acertou=False
palpite=0
while not acertou:
    j=int(input('qual seu palpite? '))
    palpite+=1
    if j == pc:
        acertou=True
    else:
        if j < pc:
            print('mais...')
        elif j > pc:
            print('menos...')
print('acertou com {} palpites'.format(palpite))
