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


    while True:
        peso = input('Peso:')
        if peso.isalpha() == False and peso.isalnum() == True:
            pessoa.append(peso)
            peso = float(peso)
            break
        else:
            print('peso invalido, tente novamente.')

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
print('O maior peso foi de {}Kg. Peso de '.format(maior))
print('O menor peso foi {}Kg. Peso de '.format(menor))
print(lista_pessoa)