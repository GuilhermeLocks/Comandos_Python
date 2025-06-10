while True:
    try:
        Numero_Inteiro = int(input('Digite um número inteiro: '))
    except UnicodeDecodeError:
        print('\nO usuário preferido não digitar o valor. ')
        break
    except:
        print('ERRO! Digite um valor válido.')
    try:
        Numero_Quebrado = float( input('Digite um número com vírgula:'))
    except UnicodeDecodeError:
        print('\nO usuário preferido não digitar o valor. ')
        break
    except:
        print('ERRO! Digite um valor válido.')
    else:
        break