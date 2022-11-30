import moeda

p=float(input('digite o preco: R$ '))
print(f'a metade de R$ {moeda.moeda(p)} e R$ {(moeda.metade(p,True))}')
print(f'o dobro de R$ {moeda.moeda(p)} e R$ {(moeda.dobro(p,True))}')
print(f'aumentando 10% temos R$ {(moeda.aumentar(p,10, True))}')
print(f'reduzindo 10% temos R$ {moeda.diminuir(p,10, True)}')
