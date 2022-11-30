#print(input.__doc__)
#help(input) - sao mesma coisa

'''def contador (i,f,p):
    """
    => faz uma contagem e mostra na tela:
    :param i:inicio da contagem
    :param f:final da contagem
    :param p:passo da contagem
    :return:sem retorno
    """
    c=i
    while c <= f:
        print(f'{c} ', end='')
        c+=p
    print('FIM')

contador(2,10,2)
help(contador)'''

'''def soma(a=0,b=0,c=0):#0== parametro opcional para funcionar o programa
    """
    =>faz a soma de 3 valores
    :param a:primeiro valor
    :param b:segundo valor
    :param c:terceiro valor
    created by |Giordanni
    """
    soma=a+b+c
    print(f'a soma dos valores sao {soma}')

soma(10,80,5)'''

'''def funcao():
    n1=4 #escopo local
    print(f'n1 DENTRO vale {n1}')

#programa principal(escopo global)
n1=2
funcao()
print(f'n1 FORA vale {n1}')'''

'''def soma(a=0,b=0,c=0):
    #global a => significa para usar o 'a' global, e nao usar o 'a' local
    s=a+b+c
    return s #=> para escrever separado na hora que roda o programa

r1= soma (2,4,6)
r2= soma (2,2)
r3= soma (3)
print(f'os resultados foram {r1}, {r2} e {r3}')'''

'''def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f *=c
    return f

n=int(input('digite um numero: '))
print(f'o fatorial de {n} e {fatorial(n)}')'''

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num=int(input('vlaor: '))
if par(num):
    print('e par')
else:
    print('nao e par')