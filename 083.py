ex=str(input('expressao: '))
pilha=[]
for sim in ex:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('correto')
else:
    print('errado')
