from datetime import datetime
dados=dict()
dados['nome']= str(input('nome: '))
nasc=int(input('data de nasc.: '))
dados['idade']= datetime.now().year - nasc
dados['ct']=int(input('carteira de trabalho (0 nao tem): '))
if dados['ct'] != 0:
    dados['contratacao']=int(input('ano de contratacao: '))
    dados['salario']=float(input('salario: R$ '))
    dados['aposentadoria']= dados['idade'] + dados['contratacao'] + 35 - datetime.now().year
print('-='*20)
print(dados)
for k,v in dados.items():
    print(f'    - {k} tem o valor {v}')
