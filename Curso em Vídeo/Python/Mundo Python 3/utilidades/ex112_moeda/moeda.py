def leiadinheiro(moeda, b, c):
    while moeda.isalpha() == True or moeda.isalnum() == True:
        if moeda.isnumeric() == True:
            break
        print('ERRO: {} é um preço inválido!1'.format(moeda))
        moeda = input('Digite o preço: R$')

    if moeda.isnumeric() == True:
        moeda = int(moeda)
        print('-' * 30)
        print('       RESUMO DO VALOR ')
        print('-' * 30)
        preco = '{:.2f}'.format(moeda)
        print('Preço analizado:', preco)
        preco = moeda
        preco = '{:.2f}'.format(preco / 2)
        print('Metade do preço:', preco)
        preco = moeda
        preco = '{:.2f}'.format(preco * 2)
        print('Dobro do preço:', preco)
        preco = moeda
        preco = '{:.2f}'.format((preco / 100) * (100 + b))
        print('{}% de aumento:'.format(b), preco)
        preco = moeda
        preco = '{:.2f}'.format((preco / 100) * (100 - c))
        print('{}% de desconto:'.format(c), preco)
        return

    if ',' in moeda:
        moeda = moeda.replace(',', '.')
    moeda = float(moeda)

    if moeda == float(moeda):
        print('-' * 30)
        print('       RESUMO DO VALOR ')
        print('-' * 30)
        preco = '{:.2f}'.format(moeda)
        print('Preço analizado:', preco)
        preco = moeda
        preco = '{:.2f}'.format(preco / 2)
        print('Metade do preço:', preco)
        preco = moeda
        preco = '{:.2f}'.format(preco * 2)
        print('Dobro do preço:', preco)
        preco = moeda
        preco = '{:.2f}'.format((preco / 100) * (100 + b))
        print('{}% de aumento:'.format(b), preco)
        preco = moeda
        preco = '{:.2f}'.format((preco / 100) * (100 - c))
        print('{}% de desconto:'.format(c), preco)
        return






