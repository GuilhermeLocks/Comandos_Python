def contador(*num):
    total = 0
    print(f'A soma entre ', end='')
    for c in num:
        total += c
        print(f'{c}, ' , end='')
    print(f'é iqual a {total}.')

def dobra(*ex):
    total = []
    for c in ex:
        total.append(c * 2)
    print(f'O dobro de {ex} é iqual a {total}.')

contador(2, 1, 7)
contador(8, 8)
contador(4, 4, 7, 6, 2)
print()
dobra(2, 1, 7)
dobra(8, 8)
dobra(4, 4, 7, 6, 2)
