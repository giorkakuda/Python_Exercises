a=int(input('digite o ano '))
if a % 4==0 and a % 100 !=0 or a % 400==0:
    print('o ano é bissexto')
else:
    print('o ano não e bissexto')
