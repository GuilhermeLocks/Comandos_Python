print('-'*40)
print('          LOJA SUPER BARATÃO          ')
print('-'*40)
maior_preco = menor_preco = total = caro = 0
produto = barato = ''
while True:

#recebe e valida o produto

    while True:
        produto = input('Nome do Produto: ')
        if produto.isalpha() == True:
            produto = str(produto)
            break
        else:
            print('Produto invalido, tente novamente.')

#recebe e valida o preço

    while True:
        preco = input('Preço: R$ ')
        if preco.isnumeric() == True:
            preco = int(preco)
            total += preco
            break
        else:
            print('Preço invalido, tente novamente.')

#verifica se o valor e maior que 1000

    if preco > 1000:
        caro += 1

#verifica o produto mais barato

    if menor_preco == 0:
        menor_preco = preco
        barato = produto
    if preco < menor_preco:
        menor_preco = preco
        barato = produto

#pergunta se quer continuar

    continuar = input('Quer continuar? [S/N]').upper()
    if continuar == 'N' or continuar == 'S':
        if continuar == 'N':
            break
    else:
        print('Comando invalido, tente novamente')

print('---------- FIM DO PROGRAMA ----------')
print('O total da compra foi R${}'.format(total))
print('Temos {} produtos custando mais de R$1000.00'.format(caro))
print('O produto mais barato foi {} que custava R${}'.format(barato, menor_preco))