from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a=open(nome, 'wt+')# + faz a diferenca
        a.close()
    except:
        print('houve um erro na criacao')
    else:
        print(f'arquivo {nome} criado com sucesso')


def ler(nome):
    try:
        a=open(nome, 'rt')
    except:
        print('erro ao ler um arquivo')
    else:
        cabecalho('Pessoas cadastradas')
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a=open(arq, 'at')
    except:
        print('houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('erro na hora de escrever os dados')
        else:
            print(f'novo cadastro de {nome} adicionado')
            a.close()
