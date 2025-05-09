lista_pessoa = []
pessoa = []
continuar = ''
cont = 0
maior = menor = 0
while continuar != 'N':

    while True:
        nome  = input('Nome:')
        if nome.isalpha() == True:
            pessoa.append(nome)
            break
        else:
            print('nome invalido, tente novamente.')

    peso = float(input('Peso:'))
    pessoa.append(peso)

    if maior < peso:
        maior = peso

    if menor == 0:
        menor = peso

    if menor > peso:
        menor = peso

    lista_pessoa.append(pessoa[:])
    cont += 1
    pessoa.clear()

    while True:
        continuar = input('Quer continuar? [S/N]').upper()
        if continuar == 'N':
            break
        elif continuar == 'S':
            break
        else:
            print('Comando invalido, tente novamente')
print('Ao todo, você cadastrou {} pessoas.'.format(cont))
print('O maior peso foi de {}Kg. Peso de '.format(maior), end=' ')
for c in lista_pessoa:
    if c[1] == maior:
        print(c[0], end=' ')
print('')
print('O menor peso foi {}Kg. Peso de '.format(menor), end=' ')
for c in lista_pessoa:
    if c[1] == menor:
        print(c[0], end=' ')
print('')