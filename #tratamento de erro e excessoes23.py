'''try:
    a= int(input('1 numero: '))
    b= int(input('2 numero: '))
    c= a / b
except Exception as erro:
    print(f'o problema encontrado foi {erro.__class__}')
else: #esse é o tratamento de erro
    print(f' o resultado e {c}')
finally:# acontence independente se deu certo ou erro (else e finally sao opcionais)
    print('volte sempre obrigado!!')'''

try:
    a= int(input('1 numero: '))
    b= int(input('2 numero: '))
    c= a / b
except (ValueError,TypeError):
    print('o problema com tipo de dados')
except ZeroDivisionError:
    print('nao é possivel dividir por zero')
except KeyboardInterrupt:
    print('usuario nao informou os dados')
except Exception as erro:
    print(f'o erro encontrado foi {erro.__cause__}')
else: #esse é o tratamento de erro
    print(f' o resultado e {c}')
finally:# acontence independente se deu certo ou erro (else e finally sao opcionais)
    print('volte sempre obrigado!!')
