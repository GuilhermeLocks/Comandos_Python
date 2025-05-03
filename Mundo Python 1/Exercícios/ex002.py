while True:
    nome = input('Digite seu nome: ')
    if nome.isalpha() == True:
        nome = str(nome)
        break
    else:
        print('Nome invalido, tente novamente.')
print('É um prazer te conhecer, {}!'.format(nome))
