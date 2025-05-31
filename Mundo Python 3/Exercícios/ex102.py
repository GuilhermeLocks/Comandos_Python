def fatorial(a, show=False):
    cont = 1
    for c in range(1, a+1):
        cont *= c
        if c != a:
            if show:
                print(c, end=' x ')
        else:
            if show:
                print(c, end=' = ')
    print(cont)
fatorial(5, show=True)