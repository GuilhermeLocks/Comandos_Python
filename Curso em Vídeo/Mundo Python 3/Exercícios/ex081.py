lista = []
cont = 0
continuar = ''
while continuar != 'N':

    while True:
        valor = (input('Digite um valor: '))
        if valor.isnumeric() == True:
            valor= int(valor)
            lista.append(valor)
            cont += 1
            break
        else:
            print('Valor invalido, tente novamente.')

    while True:
        continuar = input('Quer continuar? [S/N]').upper()
        if continuar == 'S':
            continuar = 'S'
            break
        elif continuar == 'N':
            continuar = 'N'
            break
        elif continuar != 'S' and continuar != 'N':
            print('Comando invalido, tente novamente.')

print('Você digitou {} elementos'.format(cont))
lista.sort(reverse=True)
print('Os valores em ordem decrescente sâo {}'.format(lista))
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')