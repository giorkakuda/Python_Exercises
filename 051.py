p=int(input('primeiro termo: '))
r=int(input('razao: '))
d= p + (10-1) * r #formula
for c in range(p, d +r , r,):
    print(c, end='=')
print('fim')

