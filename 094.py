galera=list()
pessoa=dict()
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome']= str(input('Nome: '))
    while True:
        pessoa['sexo']= str(input('Sexo(MF): ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO, digite "M" ou "F"')
    pessoa['idade']=int(input('idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('continua(S/N)?')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO responda "S" ou "N"')
    if resp == 'N':
        break

print(f'A) o total de cadastrados sao {len(galera)}')# criei uma lista de dicionarios
media=soma / len(galera)
print(f'B) a media de idade e de {media:5.2f} anos')
print('C) as mulheres cadastradas sao: ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}')
print('D) lista das pessoas acima da media')
for p in galera:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}')
        print()
print('FIM')