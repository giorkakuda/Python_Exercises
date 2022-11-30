'''num= [2,5,9,1]
num [2] = 3
num.append(7)
num.reverse()
num.sort(reverse=True)
num.insert(4,0)
#num.pop(4)
if 2 in num:
    num.remove(2)
else:
    print('nao existe 4')
print(num)
print(f'essa lista tem {len(num)} elementos')'''

'''valores=[]
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for cont in range(1,5):
    valores.append(int(input('digite o valor: ')))
for c, v in enumerate(valores):
    print(f'na posicao {c} encontrei {v}')'''

a=[2,3,4,7]
#b=a #ligacao, altera os 2
b=a[:]
b[2]=2 #copia
print(f'{a}')
print(f'{b}')