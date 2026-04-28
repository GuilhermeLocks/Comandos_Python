def LeiaInt(a):
    while True:
        if a.isnumeric() == True:
            return a
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            a = input('Digite um número: ')
LeiaInt(input('Digite um número: '))