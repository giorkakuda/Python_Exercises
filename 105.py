def notas(*n, sit=False):
    """
    => funcoes para analisar notas e situacoes
    :param n: uma ou mais notas de alunos
    :param sit:valor opcional, adiciona ou nao a situacao
    :return:dicionario com varias situacoes de alunos
    """
    r = dict()
    r['total']= len(n)
    r['maior']= max(n)
    r['menor']= min(n)
    r['media']= sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao']= 'boa'
        elif r['media'] >= 5:
            r['situacao']= 'razoavel'
        else:
            r['situacao']='ruim'


    return r

#programa principal
#resp = notas(5.5,2.5,7, sit=True)
#print(resp)
help(notas)
