numero= int(input('Digite um número: '))
contador = 0
print('Divisores: ', end='')
for c in range(1, numero+1):
    if numero == int(numero / c)*c:
        print(c, end = ' ')
        contador += 1
print()
if contador == 2:
    print('É um número primo')
elif contador >= 3:
    print('Não é um número primo.')

