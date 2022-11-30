f=str(input('digite e frase ')).strip().upper()
print('a frase aparece ''A'' {} vezes'.format(f.count('A')))
print('a primeira letra ''A'' apareceu na posicao {}'.format(f.find('A')+1))
print('a ultima letra ''A'' apareceu na posicao {}'.format(f.rfind('A')+1))
