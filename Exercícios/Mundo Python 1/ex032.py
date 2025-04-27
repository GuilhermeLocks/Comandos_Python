n1 = int(input('digite o ano: '))
n2 = n1 / 4
n3 = n1 / 100
n4 = n1 / 400
n5 = 0
n6 = 0

if n3 == int(n3) and n4 == int(n4):
     print('bissexto1')
     n5 += 1
     n6 += 1

if n5 == 0 and n2 == int(n2):
    print('bissexto2')
    n6 += 1

if n6 == 0:
    print('nao e bissexto')

