n1 = int(input('valor: '))
n2 = int(input('valor: '))
n3 = int(input('valor: '))
n4 = 0
n5 = 0

if n1 > n2 and n1 > n3:
    n4 = n1
    print(n4)
if n2 > n1 and n2 > n3:
    n4 = n2
    print(n4)
if n3 > n2 and n3 > n1:
    n4 = n3
    print(n4)

if n1 < n2 and n1 < n3:
    n5 = n1
    print(n5)
if n2 < n1 and n2 < n3:
    n5 = n2
    print(n5)
if n3 < n2 and n3 < n1:
    n5 = n3
    print(n5)