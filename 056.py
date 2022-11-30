somaidade=0
maioridade=0
nomevelho=" "
totm=0
for p in range(1,5):
    print('===== {} pessoa ====='.format(p))
    n=str(input('Nome: ')).strip().lower()
    i=int(input('idade: '))
    s=str(input('sexo(M/F): ')).strip().lower()
    somaidade=somaidade+i
    media = somaidade / 4

    if p == 1 and s in "Mm":
        maioridade=i
        nomevelho=n
    if s in 'Mm' and i > maioridade:
        maioridade=i
        nomevelho=n
    if s in 'Ff' and i <20:
            totm+=1

print('a media de idade e {}'.format(media))
print('o nome do homem mais velho e {} e idade e {} anos'.format(nomevelho, maioridade))
print('o numero de mulher com menos de 20 anos e {}'.format(totm))
