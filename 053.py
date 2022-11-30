frase=str(input('frase: ')).strip().lower()
palavra=frase.split()
junto='' .join(palavra)
inverso=junto[::-1]
print('o inverso de {} e {}'.format(junto, inverso))
#inverso=''
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} e {}'.format(junto, inverso))'''
if inverso==junto:
    print('temos palindromo')
else:
    print('nao temos palindromo')

