def contador(a):
    n = 0
    for c in a:
        n += 1
    print(f'Essa palavra tem {n} caracteres.')

contador(input('Digite uma palavra:'))