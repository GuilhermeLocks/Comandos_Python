tupla = (1, 'X', 3, 'Y')
for c in tupla:
    print(c, end=' ')
print('')
lista = [2, 'X', 4, 'Y']
for c in lista:
    print(c, end=' ')
print('')
lista.append('W')
for c in lista:
    print(c, end=' ')
lista.insert(4, 5)
print('')
for c in lista:
    print(c, end=' ')
del lista[2]
lista.pop(2)
lista.remove('W')
print('')
for c in lista:
    print(c, end=' ')
print('')
valores = list(range(1, 11))
for c in valores:
    print(c, end=' ')
print('')
valor = [5, 6, 8, 9, 3, 4, 2, 7, 1, 10, 0]
for c in valor:
    print(c, end=' ')
print('')
valor.sort()
for c in valor:
    print(c, end=' ')
print('')
valor.sort(reverse=True)
for c in valor:
    print(c, end=' ')
print('')
valor.sort()
print(len(valor))
for c, v in enumerate(valor):
    print('Na posição {} encontrei o valor {}!'.format(c, v))