n1 = int(input('Valor da casa: R$'))
n2 = int(input('Salário do comprador: R$'))
n3 = int(input('Quantos anos de financiamento? '))
n4 = n3*12
n5 = n1/n4
if n5 <= (n2/100)*30:
    print('ok', n5)