while True:
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
        except UnicodeDecodeError:
            print('\nO usuário preferido não digitar o valor. ')
            break
        except:
            print('\033[31mERRO! por favor, digite um valor inteiro válido.\033[m')
        else:
            break
    try:
        real = float( input('Digite um número com vírgula:'))
    except UnicodeDecodeError:
        print('\n\033[31mO usuário preferido não digitar o valor. \033[m')
        real = 0
        print('O valo inteiro digitado foi {} e o real foi {}'.format(inteiro, real))
        break
    except:
        print('\033[31mERRO! por favor, digite um valor inteiro válido.\033[m')
    else:
        print('O valo inteiro digitado foi {} e o real foi {}'.format(inteiro, real))
        break