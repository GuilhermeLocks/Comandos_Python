while True:
    n1 = input('Qual é o salário do funcionário? R$')
    if n1.isnumeric() == True:
        n1 = float(n1)
        break
    else:
        print('Salário invalido, tente novamente.')
print('Um funcionário que ganha R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(n1, (n1/100)*115))