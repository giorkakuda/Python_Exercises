aluno=dict()
aluno['nome']=str(input('nome: '))
aluno['media']=float(input(f'media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao']= 'aprovado'
elif 5<= aluno['media'] <7:
    aluno['situacao']= 'recuperacao'
else:
    aluno['situacao']= 'reprovado'
print('=-'*20)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
