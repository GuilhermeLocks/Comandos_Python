n1 = []
n1 = input('Informe um número:')

n2 = len(n1)-1
n3 = len(n1)-2
n4 = len(n1)-3
n5  = len(n1)-4

if n2 >= 0:
    print(f'Unidade:{n1[n2]}')
if n3 >= 0:
    print(f'Dezena:{n1[n3]}')
if n4 >= 0:
    print(f'Centena:{n1[n4]}')
if n5 >= 0:
    print(f'Milhar:{n1[n5]}')
