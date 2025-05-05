lista = []
continuar = ''
while continuar != 'N':
    while True:
        valor = input('Digite um valor: ')
        if valor.isnumeric() == True:
            if valor in lista:
                print('Valor duplicado! Não vou adicionar...')
            else:
                lista.append(valor)
                break
        else:
            print('Valor invalido, tente novamente')
    while True:
        continuar = input('Quer continuar? [S/N]').upper()
        if continuar != 'N' and continuar != 'S':
            print('Comando invalido, tente novamente.')
        elif continuar == 'S' or continuar == 'N':
            break

print('-='*40)
print('Você digitou os valores {}'.format(lista))