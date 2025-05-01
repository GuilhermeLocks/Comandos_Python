lista = 'lÁPIS', '1.75', 'Borracha', '2.50', 'Tenis', '99.98'
print('-'*45)
print('             LISTAGEM DE PREÇOS')
print('-'*45)
for c in range(0, len(lista), 2):
    print(lista[c], end='')
    print('.'*(30-len(lista[c])), end='')
    print('R$', end='')
    print(' '*(8-len(lista[c+1])), end='')
    print(lista[c+1])
print('-'*45)