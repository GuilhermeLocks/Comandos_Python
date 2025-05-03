while True:
    n1= input('Quanto dinheiro você tem na carteira? R$')
    if n1.isnumeric() == True:
        n1 = float(n1)
        break
    else:
        print('Valor invalido, tente novamente.')
print('Com {:.2f} você pode comprar US${:.2f}'.format(n1, (n1/6)))