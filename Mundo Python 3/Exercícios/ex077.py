lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM')
for c in range(0, len(lista)):
    print('\nNa palavra {} temos'.format(lista[c]), end=' ')
    lista_2 = lista[c]
    for c in lista_2:
        if 'A' in c:
            print('A', end=' ')
        if 'E' in c:
            print('E', end=' ')
        if 'I' in c:
            print('I', end=' ')
        if 'O' in c:
            print('O', end=' ')
        if 'U' in c:
            print('U', end=' ')