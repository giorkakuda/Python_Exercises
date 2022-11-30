'''def lin():
    print('-'*30)

lin()
print('   CURSO EM VIDEO')
lin()
print('     aprenda Python')
lin()
'''
'''def titulo(txt):
    print('_'*30)
    print(txt)
    print('_'*30)

titulo('CURSO EM VIDEO')
#titulo('aprenda Python')'''

'''def soma(a,b):
    s=a+b
    print(s)

soma (2,2)
soma (3,3)
soma (9,9)'''

'''def soma(a,b):
    print(f'A = {a} e B = {b}')
    s=a+b
    print(f'a soma de A+B = {s}')

soma (b=5,a=2)
soma (a=3,b=9)
soma (9,9)'''

#def contador(*num):
 #   print(num)# agora ele cria TUPLAS, (    )
#contador(2,4,5,4)
#contador(5,3,1)


'''def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('=>FIM')
contador(2, 4, 5, 4)
contador(5, 3, 1)'''

'''def contador(*num):
    tam=len(num)
    print(f'os valores sao {num} e o total sao {tam}')
contador(2,4,5,4)
contador(5,3,1)'''


'''def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1
valores=[2,4,6]
dobra(valores)
print(valores)'''

def soma(*valores):
    s=0
    for num in valores:
        s +=num
    print(f'somando {valores} temos {s}')
soma(5,2)
soma(4,2,1,9)

