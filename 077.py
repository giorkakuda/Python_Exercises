palavras= ('aprender', 'programar', 'linguagem', 'python',
           'curso', 'gratis', 'aprender', 'praticar',
           'trabalhar', 'programar', 'mercado', 'futuro')
for p in palavras:
    print(f'\n as vogais na palavra {p} sao:',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end='')
