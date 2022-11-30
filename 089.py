lista=list()

while True:
    n=str(input('nome: '))
    n1=float(input('nota1: '))
    n2=float(input('nota2: '))
    m= (n1+n2) / 2
    lista.append([n, [n1,n2], m])
    r=str(input('continua:(S/N) ')).strip().upper()
    if r in 'Nn':
        break
print(f'{"N°":<4}{"Nome":<10}{"Media":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')

while True:
    opc=int(input('mostrar nota do aluno:(999 interrompa) '))
    if opc == 999:
        print('finalizando...')
        break
    if opc <= len(lista)-1:
        print(f'notas de {lista [opc][0]} sao {lista [opc] [1]}')
