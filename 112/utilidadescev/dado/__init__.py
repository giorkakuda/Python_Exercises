def leiadinheiro(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada =='':
            print(f'\033[0:31mErro,\"{entrada}\" e um preco invalido\33[m')
        else:
            valido=True
            return float(entrada)
