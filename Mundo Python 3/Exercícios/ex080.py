valor = []
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    valor.append(numero)
    valor.sort()
    if valor[len(valor)-1] == numero:
        print('Adicionado ao final da lista...')
    else:
        print('Adicionado na posição {} da lista...'.format(valor.index(numero)))
print('-='*40)
print('Os valores digitados em ordem foram {}'.format(valor))