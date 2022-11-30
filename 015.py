#km= R$0.15
#dias= R$60.00
k=float(input('km rodado: '))
d=int(input('qtos dias: '))
p= (k * 0.15) + (d * 60)
print('o cliente rodou {}km por {} dias e pagara {:.2f}'.format(k, d, p))
