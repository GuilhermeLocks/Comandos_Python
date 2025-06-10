while True:
    try:
        Numero_Inteiro = int(input('Digite um número inteiro: '))
    except KeyboardInterrupt:
        print('O usuário preferido não digitar o valor. ')
    except:
        print('ERRO! Digite um valor válido.')
    else:
        break
while True:
    try:
        Numero_Quebrado = float( input('Digite um número com vírgula:'))
    except KeyboardInterrupt:
        print('O usuário preferido não digitar o valor. ')
    except:
        print('ERRO! Digite um valor válido.')
    else:
        break