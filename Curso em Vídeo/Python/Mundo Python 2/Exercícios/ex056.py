soma = 0
velho = 0
senhor = ''
novas = 0
for c in range(1, 5):
    print('-'*4, c, 'PESSOA', '-'*4)

    nome = input('Digite seu nome: ')
    idade = int(input('Idade:'))
    sexo = input('Sexo [M/F]: ').upper()

    if sexo == str('M'):
        if idade > velho:
            velho = idade
            senhor = nome

    if sexo == str('F'):
        if idade < 20:
            novas += 1

    soma += idade

media = soma / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos de idade e se chama {}'.format(velho, senhor))
print('Ao todo são {} mulheres com menos de 20 anos'.format(novas))