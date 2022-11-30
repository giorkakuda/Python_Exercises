from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq= 'curso em video.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta= menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta ==1:
        # opcao de listar o conteudo de um arquivo
        ler(arq)
    elif resposta ==2:
        # opcao de cadastrar uma pessoa
        cabecalho('Novo cadastro')
        nome=str(input('Nome: '))
        idade=leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho('saindo do programa')
        break
    else:
        print('\033[31mERRO, digite opcao valida\033[m')
    sleep(2)
