p=float(input('peso:(kg) '))
a=float(input('altura:(m) '))
imc = p / (a**2)
print('o seu imc e {:.2f}'.format((imc)))
if imc<18.5:
    print('abaixo do peso')
elif 18.5<= imc < 25:
    print('peso ideal')
elif 25<= imc <30:
    print( 'sobre peso')
elif 30<= imc<40:
    print('obesidade')
elif imc>=40:
    print('obesidade morbida')
