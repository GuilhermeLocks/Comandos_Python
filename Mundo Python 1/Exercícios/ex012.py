while True:
    n1 = input('Qual é o preço do produto? R$' )
    if n1.isnumeric() == True:
        n1 = float(n1)
        break
    else:
        print('Preço do produto, invalido tente novamente.')
print('o produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}'.format(n1, 5, (n1/100)*95))