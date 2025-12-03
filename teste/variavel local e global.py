def teste(b):
    a = 8
    b += 4
    c = 2

    lista = [a, b, c]

    return lista

a = 5
lista = []

print('Lista local:')
for c in teste(a):
    print(c)
    lista.append(c)

print('')

print(f'Lista global:{lista}')