while True:
    valor = float(input('Digite um valor: '))
    print(bool(type(valor)))
    if type(valor) == 'float':
        print('oi')
        if valor.isnumeric() == True:
            valor = int(valor)
            print('É um numero')
            break
        elif valor.isalpha() == True:
            valor = str(valor)
            print('É uma palavra')
        elif valor.isalnum() == True:
            valor = str(valor)
            break
            print('É um numero, palavra')
        else:
            print('ERRO!', type(valor))