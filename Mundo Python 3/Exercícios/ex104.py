def LeiaInt(a):
    while True:
        if a.isnumeric() == True:
            return a
        else:
            print('ERRO')
            a = input('Digite um número: ')


LeiaInt(input('Digite um número: '))