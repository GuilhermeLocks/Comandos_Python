n1 = float(input('Qual é o preço do produto? R$' ))
print('o produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}'.format(n1, 5, (n1/100)*95))