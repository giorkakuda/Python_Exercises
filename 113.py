def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO digite numero inteiro\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31minterrompido pelo usuario\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError, TypeError):
            print('\033[35mdigite numero real\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[35minterrompido pelo usuario\033[m')
            return 0
        else:
            return n


n1=leiaInt('numero inteiro:')
n2=leiaFloat('numero real: ')
print(f' o valor inteiro foi {n1} e o real foi {n2}')

