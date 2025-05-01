cont = 0
total = 0
maior = 0
menor = 0

while True:

    valor = input('Digite um número: ')

    if valor.isnumeric() == True:
        valor = int(valor)
        total += valor
        cont += 1

    if valor > maior:
        maior = valor

    if menor == 0:
        menor = valor

    if menor > valor:
        menor = valor

    else:
        print('Invalido, tente novamente.')
    continuar = input('Quer continuar? [S/N]: ').upper()

    if continuar == 'N':
        print('Você digitou {} números e a média foi {:.2f}'.format(cont, total/cont))
        print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
        break

    elif continuar != 'S' and continuar != 'N':
        print('Comando invalido, tente novamente.')

