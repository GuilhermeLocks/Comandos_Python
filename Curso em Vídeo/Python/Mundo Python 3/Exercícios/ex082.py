lista_total = []
lista_impar = []
lista_par = []
continuar = ''
while continuar != 'N':
    while True:
        numero = input('Digite um número: ')
        if numero.isnumeric() == True:
            numero = int(numero)
            lista_total.append(numero)
            break
        else:
            print('Número invalido, tente novamente.')
    while True:
        continuar = input('Quer continuar? [S/N] ').upper()
        if continuar == 'N':
            continuar = 'N'
            break
        elif continuar == 'S':
            break
        elif continuar != 'N' and continuar != 'S':
            print('Comando invalido, tente novamente.')
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
print('A lista completa é {}'.format(lista_total))
print('A lista de pares é {}'.format(lista_par))
print('A lista de ímpares é {}'.format(lista_impar))