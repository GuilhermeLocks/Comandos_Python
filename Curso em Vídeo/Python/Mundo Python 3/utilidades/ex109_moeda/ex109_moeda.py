def metade(a, b):
    if b is True:
        a = '{:.2f}'.format(a/2)
        return a
    else:
        a = a/2
        return a
def dobro(a, b):
    if b is True:
        a ='{:.2f}'.format(a*2)
        return a
    else:
        a = a*2
        return a
def formatar(a, b):
    if b is True:
        a = '{:.2f}'.format(a)
        return a
    else:
        a = a
        return a

def aumentar(a, b, c):
    if b is True:
        a = '{:.2f}'.format((a/100)*(100+c))
        return a
    else:
        a = ((a/100)*(100+c))
        return a
def reduzir(a, b, c):
    if b is True:
        a = '{:.2f}'.format((a/100)*(100-c))
        return a
    else:
        a = ((a/100)*(100-c))
        return a
