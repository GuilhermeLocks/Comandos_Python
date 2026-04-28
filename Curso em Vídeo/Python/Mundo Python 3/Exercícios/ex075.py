pares = []
while True:
    valor_1 = input('Digite um valor: ')
    if valor_1.isnumeric() == True:
        valor_1 = int(valor_1)
        if valor_1 % 2 == 0 and valor_1 != 0:
            pares.append(valor_1)
        break
    else:
        print('Valor invalido, tente novamente.')
while True:
    valor_2 = input('Digite um valor: ')
    if valor_2.isnumeric() == True:
        valor_2 = int(valor_2)
        if valor_2 % 2 == 0 and valor_2 != 0:
            pares.append(valor_2)
        break
    else:
        print('Valor invalido, tente novamente.')
while True:
    valor_3 = input('Digite um valor: ')
    if valor_3.isnumeric() == True:
        valor_3 = int(valor_3)
        if valor_3 % 2 == 0 and valor_3 != 0:
            pares.append(valor_3)
        break
    else:
        print('Valor invalido, tente novamente.')
while True:
    valor_4 = input('Digite um valor: ')
    if valor_4.isnumeric() == True:
        valor_4 = int(valor_4)
        if valor_4 % 2 == 0 and valor_4 != 0:
            pares.append(valor_4)
        break
    else:
        print('Valor invalido, tente novamente.')
lista = valor_1, valor_2, valor_3, valor_4
print('Você digitou os valores {}'.format(lista))
print('O valor 9 apareceu {} vezes'.format(lista.count(9)))
if 3 in lista:
    print('O valor 3 apareceu {}° posição'.format(lista.index(3)+1))
else:
    print('O valor 3 não apareceu na lista')
print('Os valores pares digitados foram {}'.format(pares))