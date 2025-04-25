jogadas_diponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
linha_11 = '1'
linha_12 = '2'
linha_13 = '3'
linha_21 = '4'
linha_22 = '5'
linha_23 = '6'
linha_31 = '7'
linha_32 = '8'
linha_33 = '9'
result = ''
while True:

    #jogo

    print('-'*30)
    print('         JOGO DA VELHA          ')
    print('-'*30)
    print('''
            {}  |  {}  |  {}
          -----------------
            {}  |  {}  |  {}
          -----------------
            {}  |  {}  |  {}
    '''.format(linha_11, linha_12, linha_13, linha_21, linha_22, linha_23, linha_31, linha_32, linha_33))
    print('-'*30)

    #recebe jogada

    while True:
        jogada = input('Qual sua jogada? ')
        if jogada.isnumeric() == True:
            jogada = int(jogada)
            if jogada in jogadas_diponiveis:
                jogada = int(jogada)
                break
            else:
                print('Essa posição ja esta oculpada, tente novamente')
        else:
            print('Jogada invalida tente novamente')

    # realiza a jogada

    for c in range(1, 10):
        if jogada == c:
            if c in jogadas_diponiveis:
                jogadas_diponiveis.remove(c)
                if c == 1:
                    linha_11 = 'x'
                if c == 2:
                    linha_12 = 'x'
                if c == 3:
                    linha_13 = 'x'
                if c == 4:
                    linha_21 = 'x'
                if c == 5:
                    linha_22 = 'x'
                if c == 6:
                    linha_23 = 'x'
                if c == 7:
                    linha_31 = 'x'
                if c == 8:
                    linha_32 = 'x'
                if c == 9:
                    linha_33 = 'x'

    # verifica se alguem ganhou

    if linha_11 == linha_12 == linha_13:
        if linha_11 == 'x':
            result = 'x'
            break
        elif linha_11 == 'o':
            result = 'o'
            break
    elif linha_21 == linha_22 == linha_23:
        if linha_21 == 'x':
            result = 'x'
            break
        elif linha_21 == '0':
            result = 'o'
            break
    elif linha_31 == linha_32 == linha_33:
        if linha_31 == 'x':
            result = 'x'
            break
        elif linha_31 == 'o':
            result = 'o'
            break
    elif linha_11 == linha_21 == linha_31:
        if linha_11 == 'x':
            result = 'x'
            break
        elif linha_11 == 'o':
            result = 'o'
            break
    elif linha_12 == linha_22 == linha_32:
        if linha_12 == 'x':
            result = 'x'
            break
        elif linha_12 == 'o':
            result = 'o'
            break
    elif linha_13 == linha_23 == linha_33:
        if linha_13 == 'x':
            result = 'x'
            break
        elif linha_13 == 'o':
            result = 'o'
            break
    elif linha_11 == linha_22 == linha_33:
        if linha_11 == 'x':
            result = 'x'
            break
        if linha_11 == 'o':
            result = 'o'
            break
    elif linha_13 == linha_22 == linha_31:
        if linha_13 == 'x':
            result = 'x'
            break
        elif linha_13 == 'o':
            result = 'o'
            break

            
print('-'*30)
if result == 'x':
    print('jogo ganho')
elif result == 'o':
    print('jogo perdido')
print('-'*30)
print('         JOGO DA VELHA          ')
print('-'*30)
print('''
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
'''.format(linha_11, linha_12, linha_13, linha_21, linha_22, linha_23, linha_31, linha_32, linha_33))
print('-'*30)