while True:
    try:
        numero_1 = int(input('Digite o primeiro número:'))
        break
    except ValueError:
        print('Erro: Entrada inválida. Digite apenas números.')

while True:
    operacao = str(input('Escolha a operação (+, -, *, /):'))
    if numero_1 == 0 and operacao == '/':
        print('Erro: Divisão por zero não é permitida.')
    else:
        if operacao == '*' or operacao == '/' or operacao == '+' or operacao == '-':
            break
        else:
            print('Opção inválida')

while True:
    try:
        numero_2 = int(input('Digite o segundo número:'))
        if numero_2 == 0 and operacao == '/':
            print('Erro: Divisão por zero não é permitida.')
        else:
            break
    except ValueError:
        print('Erro: Entrada inválida. Digite apenas números.')

if operacao == '+':
    print(f'A soma entre {numero_1} e {numero_2} resulta em {numero_1 + numero_2}')
elif operacao == '-':
    print(f'A subtração entre {numero_1} e {numero_2} resulta em {numero_1 - numero_2}')
elif operacao == '*':
    print(f'A multiplicação entre {numero_1} e {numero_2} resulta em {numero_1 * numero_2}')
elif operacao == '/':
    print(f'A divisão entre {numero_1} e {numero_2} resulta em {numero_1 / numero_2}')
