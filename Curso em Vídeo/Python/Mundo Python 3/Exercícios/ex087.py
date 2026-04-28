lista = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
maior = pares = 0
for c in range(0, 3):
    for v in range(0, 3):
        lista[c][v] = input('DIgite um valor para [{}, {}]: '.format(c, v))
print('-='*40)
print(lista[0][0], lista[0][1], lista[0][2])
print(lista[1][0], lista[1][1], lista[1][2])
print(lista[2][0], lista[2][1], lista[2][2])
for c in range(0, 3):
    valor = int(lista[1][c])
    if valor > maior:
        maior = valor
for c in range(0, 3):
    for v in range(0, 3):
        valor = int(lista[c][v])
        if valor % 2 == 0:
            pares += valor
print('-='*40)
print('A soma dos valores pares é {}'.format(pares))
print('A soma dos valores da terceira coluna é {}'.format(int(lista[0][2])+int(lista[1][2])+int(lista[2][2])))
print('O maior valor da segunda linha é {}'.format(maior))