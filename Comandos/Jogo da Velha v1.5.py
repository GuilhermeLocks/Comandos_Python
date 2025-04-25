import random
jogadas_diponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogo = 0
jogada = 0
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

# cabeça do jogo

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

while True:

    # jogada do jogador

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

    # jogadas
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
    jogada = 1
    #verifica se alquem ganhou

    if linha_11 == linha_12 == linha_13:
        if linha_11 == 'x':
            print('-' * 30)
            print('jogo ganho')
            break
        elif linha_11 == 'o':
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_21 == linha_22 == linha_23:
        if linha_21 == 'x':
            print('-' * 30)
            print('jogo ganho')
            break
        elif linha_21 == '0':
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_31 == linha_32 == linha_33:
        if linha_31 == 'x':
            print('-' * 30)
            print('jogo ganho')
            break
        elif linha_31 == 'o':
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_11 == linha_21 == linha_31:
        if linha_11 == 'x':
            print('-' * 30)
            print('jogo ganho')
            break
        elif linha_11 == 'o':
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_12 == linha_22 == linha_32:
        if linha_12 == 'x':
            print('-' * 30)
            print('jogo ganho')
            break
        elif linha_12 == 'o':
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_13 == linha_23 == linha_33:
        if linha_13 == 'x':
            print('-' * 30)
            print('jogo ganho')
            break
        elif linha_13 == 'o':
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_11 == linha_22 == linha_33:
        if linha_11 == 'x':
            print('-' * 30)
            print('jogo ganho')
            break
        if linha_11 == 'o':
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_13 == linha_22 == linha_31:
        if linha_13 == 'x':
            print('-' * 30)
            print('jogo ganho')
            break
        elif linha_13 == 'o':
            print('-' * 30)
            print('jogo perdido')
            break

    # jogadas vencedoras do computador
    if jogada == 1:
        if linha_11 == linha_13:
            if linha_12 == '2':
                linha_12 = 'o'
                jogadas_diponiveis.remove(2)
                result = 'o'
                jogada += 1
        elif linha_11 == linha_12:
            if linha_13 == '3':
                linha_12 = 'o'
                jogadas_diponiveis.remove(3)
                result = 'o'
                jogada += 1
        elif linha_12 == linha_13:
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                result = 'o'
                jogada += 1
        elif linha_21 == linha_23:
            if linha_22 == '2':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                result = 'o'
                jogada += 1
        elif linha_21 == linha_22:
            if linha_23 == '6':
                linha_23 = 'o'
                jogadas_diponiveis.remove(6)
                result = 'o'
                jogada += 1
        elif linha_22 == linha_23:
            if linha_21 == '4':
                linha_22 = 'o'
                jogadas_diponiveis.remove(4)
                result = 'o'
                jogada += 1
        elif linha_31 == linha_33:
            if linha_32 == '8':
                linha_32 = 'o'
                jogadas_diponiveis.remove(8)
                result = 'o'
                jogada += 1
        elif linha_31 == linha_32:
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                result = 'o'
                jogada += 1
        elif linha_32 == linha_33:
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                result = 'o'
                jogada += 1
        elif linha_11 == linha_31:
            if linha_21 == '4':
                linha_21 = 'o'
                jogadas_diponiveis.remove(4)
                result = 'o'
                jogada += 1
        elif linha_11 == linha_21:
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                result = 'o'
                jogada += 1
        elif linha_21 == linha_31:
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                result = 'o'
                jogada += 1
        elif linha_12 == linha_32:
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                result = 'o'
                jogada += 1
        elif linha_12 == linha_22:
            if linha_32 == '8':
                linha_32 = 'o'
                jogadas_diponiveis.remove(8)
                result = 'o'
                jogada += 1
        elif linha_22 == linha_32:
            if linha_12 == '2':
                linha_12 = 'o'
                jogadas_diponiveis.remove(2)
                result = 'o'
                jogada += 1
        elif linha_13 == linha_33:
            if linha_23 == '6':
                linha_23 = 'o'
                jogadas_diponiveis.remove(6)
                result = 'o'
                jogada += 1
        elif linha_13 == linha_23:
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                result = 'o'
                jogada += 1
        elif linha_23 == linha_33:
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                result = 'o'
                jogada += 1
        elif linha_11 == linha_33:
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                result = 'o'
                jogada += 1
        elif linha_11 == linha_22:
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                result = 'o'
                jogada += 1
        elif linha_22 == linha_33:
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                result = 'o'
                jogada += 1
        elif linha_13 == linha_31:
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                result = 'o'
                jogada += 1
        elif linha_13 == linha_22:
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                result = 'o'
                jogada += 1
        elif linha_22 == linha_31:
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                result = 'o'
                jogada += 1

    # jogadas
    if jogada == 1:
        jogo = jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis))-1)]
        if jogo in jogadas_diponiveis:
            jogadas_diponiveis.remove(jogo)
            if jogo == 1:
                linha_11 = 'o'
                jogada += 2
            elif jogo == 2:
                linha_12 = 'o'
                jogada += 2
            elif jogo == 3:
                linha_13 = 'o'
                jogada += 2
            elif jogo == 4:
                linha_21 = 'o'
                jogada += 2
            elif jogo == 5:
                linha_22 = 'o'
                jogada += 2
            elif jogo == 6:
                linha_23 = 'o'
                jogada += 2
            elif jogo == 7:
                linha_31 = 'o'
                jogada += 2
            elif jogo == 8:
                linha_32 = 'o'
                jogada += 2
            elif jogo == 9:
                linha_33 = 'o'
                jogada += 2
        jogada -= 2

    print('-' * 30)
    print('''
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
               '''.format(linha_11, linha_12, linha_13, linha_21, linha_22, linha_23, linha_31, linha_32, linha_33))
    print(jogadas_diponiveis)
    print('-' * 30)
print('-' * 30)
print(jogada)
print(jogadas_diponiveis)
print('-' * 30)
print('''
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
           '''.format(linha_11, linha_12, linha_13, linha_21, linha_22, linha_23, linha_31, linha_32, linha_33))
print('-' * 30)