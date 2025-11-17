lista = [[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]
for o in range(0, 3):
    for c in range(0, 3):
        lista[o][c] = input('Digite:')
for c in range(0, 3):
    print('')
    for o in range(0, 3):
        print(lista[c][o], end=' ')

