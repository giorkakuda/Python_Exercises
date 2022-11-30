print('{:=^40}'.format('LOJAS KAKUDA'))
v=float(input('valor do produto: R$ '))
print('(1) a vista (dinheiro ou cheque) \33[:1:30:41m 10% desconto!\33[m')
print('(2) a vista no cartao \33[1:31:40m (5% de desconto)\33[m')
print('(3) em 2x no cartao, preco normal')
print('(4) 3x ou mais no cartao \33[1:30:41m (20% juros)\33[m')
o=int(input('qual opcao de pagamento? '))
if o==1:
    print('vc tera um desconto de 10% e sua compra ficara R${:.2f}'.format(v - (v * 10/100)))
elif o==2:
    print('vc tera 5% de desconto e sua compra ficara R$ {:.2f}'.format(v - (v * 5/100)))
elif o==3:
    par= v / 2
    print('vc pagara o preço normal de R${:.2f} em 2 x de R$ {:.2f}'.format(v, par))
elif o==4:
    q=int(input('qtas parcelas? '))
    j= (v + (v*20/100))
    total= j / q
    print('vc pagara juros de 20% e o valor da parcela sera de R$ {:.2f} e a compra ficara R$ {:.2f}'.format(total, j))
else:
    total=v
    print('opcao invalida tente novamente')
    