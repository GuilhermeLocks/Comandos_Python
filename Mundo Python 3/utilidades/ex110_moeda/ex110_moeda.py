def moeda(a, b, c):

    print('-'*30)
    print('       RESUMO DO VALOR ')
    print('-'*30)
    print('Preço analizado:', a)
    preco = a
    preco = '{:.2f}'.format(preco/2)
    print('Metade do preço:', preco)
    preco = a
    preco ='{:.2f}'.format(preco*2)
    print('Dobro do preço:', preco)
    preco = a
    preco = '{:.2f}'.format((preco/100)*(100+b))
    print('{}% de aumento:'.format(b), preco)
    preco = a
    preco = '{:.2f}'.format((preco/100)*(100-c))
    print('{}% de desconto:'.format(c), preco)
