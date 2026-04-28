lista = []
pessoa = ['gustavo', 40]
lista.append(pessoa[:])
pessoa = ['maria', 35]
lista.append(pessoa[:])
print(lista)
print(lista[0][0])
print(lista[0][1])
print(lista[1][0])
print(lista[1][1])