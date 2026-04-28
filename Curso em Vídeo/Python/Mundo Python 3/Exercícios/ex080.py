valor = []
for c in range(0, 5):
    numero = int(input('Digite um valor: '))

    if valor == []:
        valor.append(numero)
        print('Adicionado ao final da lista...')

    elif numero > valor[c-1]:
        valor.append(numero)
        print('Adicionado ao final da lista...')

    elif numero < valor[0]:
        valor.insert(0, numero)
        print('Adicionado no começo da lista...')

    else:

        for c in range(0, len(valor)):
            if numero > valor[c]:
                print('Adicionado na posição {} da lista...'.format(c + 1))
                valor.insert(c + 1, numero)

print('-=' * 40)
print('Os valores digitados em ordem foram {}'.format(valor))