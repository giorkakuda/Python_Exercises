v=float(input('valor da casa:R$ '))
s=float(input('salario:R$ '))
a=int(input('qtos anos: '))
p= v / (a * 12)
f= s * 30 / 100

print('para pagar uma casa no valor de R$ {:.2f}, em {} anos, cada parcela saira R$ {:.2f}'.format(v, a, p))

if f > p:
    print('seu emprestimo foi aprovado')
else:
    print('seu emprestimo foi negado')