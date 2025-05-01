#variavel simplis
lanche = 'pizza'
lanche = 'suco'
print(lanche)
print('')

#variavel composta tupla
lista_tupla = ('pizza', 'suco')
print(lista_tupla[1])
print(lista_tupla[-2])
print(lista_tupla[0::1])
print('')
print('Modo 1')
for c in range(0, len(lista_tupla)):
    print(lista_tupla[c])
print('')
print('Modo 2')
for c in lista_tupla:
    print(c)
print('')
print('Modo 3')
for posicao, itens in enumerate(lista_tupla):
    print(posicao, itens)
print('')
print(sorted(lista_tupla))
print('')

#variavel composta lista
lanche_lista = []
lanche_lista.append('pizza')
lanche_lista.append('suco')
print(lanche_lista)
print(lanche_lista[0])
print(lanche_lista[1])
print(lanche_lista[-2])
print(lanche_lista[-1])
print(len(lanche_lista))
for c in range(0, 2):
    print(lanche_lista[c])
for c in lanche_lista:
    print(c)
lanche_lista[1] = 'sucos'
print(lanche_lista[1])