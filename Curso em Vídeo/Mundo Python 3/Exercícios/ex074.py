import random
maior = menor = 0
valor_1 = random.randint(1,9)
valor_2 = random.randint(1,9)
valor_3 = random.randint(1,9)
valor_4 = random.randint(1,9)
valor_5 = random.randint(1,9)
tupla = valor_1, valor_2,valor_3,valor_4,valor_5
print('Os valores sorteados foram: ', end=' ')
for c in tupla:
    if maior < c:
        maior = c
    if menor == 0:
        menor = c
    if menor > c:
        menor = c
    print(c, end=' ')
print('')
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))