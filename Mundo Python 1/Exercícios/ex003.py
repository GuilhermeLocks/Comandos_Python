while True:
    n1  = input('Digite uma valor: ')
    if n1.isnumeric() == True:
        n1 = int(n1)
        break
    else:
        print('Valor invalido, tente novamente.')
while True:
    n2 = input('Digite outro valor: ')
    if n2.isnumeric() == True:
        n2= int(n2)
        break
    else:
        print('Valor invalido, tente novamente.')
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, n1 + n2))