maior = masc = mulher = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    #recebe idade e verifica se e um número
    while True:
        idade = input('Idade: ')
        if idade.isnumeric() == True:
            idade = int(idade)
            break
        else:
            print('Comando invalido, tente novamente.')

    #verifica quantas pessoas são maiores de idade
    if idade >= 18:
        maior += 1

    # recebe sexo e verifica se e M ou F
    while True:
        sexo = input('Sexo: [M/F] ').upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('Comando invalido, tente novamente.')

    #verifica quantos são M
    if sexo == 'M':
        masc += 1

    #verifica quantas são M com menos de 20 anos
    if sexo == 'M'and idade < 20:
        mulher += 1

    #pergunta se quer continuar
    while True:
        adicionar_pessoa = input('Quer continuar? [s/n]').upper()
        if adicionar_pessoa == 'N' or adicionar_pessoa == 'S':
            break
        else:
            print('Comando invalido, tente novamente:')
    if adicionar_pessoa == 'N':
            break
print('-'*30)
print('Total de pessoas com mais de 18 anos: {}'.format(maior))
print('Ao todo temos {} homens cadastrados'.format(masc))
print('Etermos {} mulheres com menos de 20 anos'.format(mulher))
print('-' * 30)
