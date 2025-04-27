novo = int(0)
while novo == 0:
    while True:
        valor = input('Digite o primeiro valor: ')
        number = valor.isnumeric()
        if number == True:
            valor = int(valor)
            break
        else:
            print('Valor informado infalido, tente novamente.')
    while True:
        valor1 = input('Digite o segundo valor: ')
        number = valor1.isnumeric()
        if number == True:
            valor1 = int(valor1)
            break
        else:
            print('Valor informado infalido, tente novamente.')
    print('''
[1] Somar
[2] multiplicar
[3] maior
[4] Novos númeroes
[5] Sair 
    ''')
    operacao = input('Qual a sua operação: ')
    if operacao == str(1):
        print('A soma: {} + {} = {}'.format(valor, valor1, valor+valor1))
    elif operacao == str(2):
        print('A multipplicação: {} X {} = {}'.format(valor, valor1, valor*valor1))
    elif operacao == str(3):
        if valor > valor1:
            print('O maior é {} e o menor é {}.'.format(valor, valor1))
        else:
            print('O maior é {} e o menor é {}.'.format(valor1, valor))
    elif operacao == str(4):
        novo = int(0)
        print('''
Insira novos valores.
''')
    elif operacao == str(5):
        novo += 1
        print('Operacao finalizada.')
    else:
        print('Opção invalida, tente novamente.')