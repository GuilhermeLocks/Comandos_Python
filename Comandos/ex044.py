while True:
    preco = float(input('Preço das compras: R$'))
    pagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção?'''))
    if pagamento == 1:
        print(f'{(preco/100)*90:.2f}')
        break
    elif pagamento == 2:
        print(f'{(preco / 100) * 95:.2f}')
        break
    elif pagamento == 3:
        print(f'{(preco / 100) * 100:.2f}')
        break
    elif pagamento == 4:
        vezes = int(input('Quantas vezes'))
        print(f'{(preco/100)*120:.2f}, {((preco/100)*120)/vezes:.2f}')
        break
    else:
        print('tente novamente')
