cont=('zero','um','dois', 'tres', 'quatro',
   'cinco', 'seis', 'sete', 'oito', 'nove',
   'dez', 'onze', 'doze', 'treze', 'catorze',
   'quinze', 'dezesseis', 'dezessete', 'dezoito',
   'dezenove', 'vinte')
q=''
while True:
    num = int(input('numero(0 a 20): '))
    if 0 <= num <= 20:
        break
print(f'vc digitou {cont [num]}')
