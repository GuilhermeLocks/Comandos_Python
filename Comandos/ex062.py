while True:
    valor = input('valor: ' )
    if valor.isnumeric() == True:
        valor = int(valor)
        break
    else:
        print('Valor invalido, tente novamente.')
while True:
    passo = input('passo: ')
    if passo.isnumeric() == True:
        passo = int(passo)
        break
    else:
        print('Passo invalido, tente novamente.')
print(valor, end=' -> ')
termos = 1
limite = 10
while termos != limite:
    termos += 1

    if termos+1 == limite:
        print(valor+(passo*termos), end='')
        print('')

    if termos+1 == limite:
        termos = limite

        limite_novo = input('''Quantos passo a mais ? [s] para sair ?
''').upper()
        if limite_novo.isnumeric() == True:
            limite += int(limite_novo)
        elif limite_novo == 'S':
            break
        else:
            print('Tente novamente.')

    else:
        print(valor+(passo*termos), end=' -> ')
