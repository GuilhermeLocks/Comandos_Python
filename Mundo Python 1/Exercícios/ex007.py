while True:
    n1 = input('Primeira nota do aluno: ')
    if n1.isnumeric() == True:
        n1 = float(n1)
        break
    else:
        print('Nota invalida, tente novamente.')
while True:
    n2 = input('Segunda nota do aluno: ')
    if n2.isnumeric() == True:
        n2 = float(n2)
        break
    else:
        print('Nota invalida, tente novamente.')
print('A média entre {} e {} é igual a {}'.format(n1, n2, (n1 + n2) / 2))