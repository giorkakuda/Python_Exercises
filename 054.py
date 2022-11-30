from datetime import date
d= date.today().year
tm=0
tmm=0
for p in range(1,8):
    n=int(input('ano de nascimento da pessoa {} '.format(p)))
    i=d-n
    if i>=65:
        tm+=1
    else:
        tmm+=1
print('o total de maior idade e {}'.format(tm))
print('o total de menor idade e {}'.format(tmm))
