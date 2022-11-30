def voto(ano):
    """
    programa para saber se o voto e obrigatorio em determinada idade    """

    from datetime import date
    atual= date.today().year
    idade=atual - ano
    if idade < 16:
        return (f'{idade} anos nao vota')
    elif 16<= idade < 18 or idade >65:
        return (f'{idade} anos voto opcional')
    else:
        return (f'{idade} anos voto obrigatorio')

nasc=int(input('ano de nascimento: '))
print(f'{voto(nasc)}')
#help(voto)