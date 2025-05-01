n1 = float(input('Qual é o preço do produto? R$'))
n2 = 5
print('o produto que custava {}, na promoção com desconto de {}% vai custar R${:.2f}'.format(n1, n2, n1-(n1/100)*n2))
print('o produto que custava {}, na promoção com desconto de {}% vai custar R${:.2f}'.format(n1, n2, n1-(n1/100)*5))
print('o produto que custava {}, na promoção com desconto de {}% vai custar R${:.2f}'.format(n1, n2, (n1/100)*95))