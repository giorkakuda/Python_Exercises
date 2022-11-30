soma=0
c=0
for i in range(1, 501, 2):
    if i % 3==0:
        c=c+1
        soma=soma+i
print('a soma e {} e {}'.format(c, soma))
