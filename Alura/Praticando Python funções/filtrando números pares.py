numeros = input('Digite os números separados por espaço:')
print('Números pares:', end =' ')
for c in numeros.split():
    if int(c) % 2 == 0:
        print(c, end =' ')