n1 = float(input('Valor:'))
n2 = float(input('Valor:'))
n3 = float(input('Valor:'))
if n1 + n2 > n3 and n3 + n1 > n2 and n2 + n3 > n1:
    print('pode fazer um triangulo')
else:
    print('nao pode fazer um triangulo')
