'''teste=list()
teste.append('gustavo')
teste.append(40)
galera=list()
galera.append(teste[:])
teste[0]='maria'
teste[1]=22
galera.append(teste[:])
print(galera) ou'''

'''galera=[['joao',33], ['maria', 44],['joaquim',50],['ana',33]]
#print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} de idade')'''

galera=list()
dado=list()#estrutura auxiliar para pegar dado e colocar na estrutura principal..galera
ma=me=0
for c in range(1,3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()# para apagar os dados enquanto faz o laco
for p in galera:
    if p[1] >=21:
        print(f'{p[0]} e maior')
        ma+=1
    else:
        print(f'{p[0]} e menor de idade')
        me+=1
print(f'o total de maior e {ma} e menor e {me}')
