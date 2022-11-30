'''pessoas= {'nome': 'Giordanni', 'sexo': 'M', 'idade':33}
del pessoas['sexo']
pessoas['nome']='leandro'
pessoas['peso']=100
#print(f'o {pessoas["nome"]} tem {pessoas ["idade"]} anos')
print(pessoas.items())
print((pessoas.keys()))
print((pessoas.values()))
for k, v in pessoas.items():#nao tem enumerate, usa items
    print(f'{k}={v}')'''

'''brasil=[]
estado1= {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2= {'UF': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])'''

estado=dict()
brasil=list()
for c in range(0,3):
    estado['UF']=str(input('unidade federativa: '))
    estado['sigla']=str(input('sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    #for k, v in e.items():
     #   print(f'o campo{k} tem valor {v}.')
    for v in e.values():
        print(v, end=' ')
    print()
