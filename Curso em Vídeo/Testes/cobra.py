from time import sleep
cobra = '8'
passo_1 = f'{cobra}    '
passo_2 = f' {cobra}   '
passo_3 = f'  {cobra}  '
passo_4 = f'   {cobra} '
passo_5 = f'    {cobra}'
lista = [passo_1, passo_2, passo_3, passo_4, passo_5]
while True:
    for c in lista:
        print(c)
        sleep(1)
    for c in range(3, 0, -1):
        print(lista[c])
        sleep(1)