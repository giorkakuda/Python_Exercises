from uteis import numeros
# todo arquivo py pode ser um modulo
# toda pasta dentro de um projeto é uma pacote

num=int(input('Digite um valor: '))
fat=numeros.fatorial(num)
print(f'fatorial de {num} e {fat}')
print(f' o dobro de {num} e {numeros.dobro(num)}')
