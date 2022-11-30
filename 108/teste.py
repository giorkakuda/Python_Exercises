import moeda

p=float(input('digite o preco: R$ '))
print(f'a metade de R$ {moeda.moeda(p)} e R$ {moeda.moeda(moeda.metade(p))}')
print(f'o dobro de R$ {moeda.moeda(p)} e R$ {moeda.moeda(moeda.dobro(p))}')
print(f'aumentando 10% temos R$ {moeda.moeda(moeda.aumentar(p,10))}')
