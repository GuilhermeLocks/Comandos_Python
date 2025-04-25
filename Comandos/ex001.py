import random
aleatorio_4 = random.randint(0, 3)
jogadas_totais = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogadas_diponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogo = 0
print('-'*30)
print('         JOGO DA VELHA          ')
print('-'*30)
linha_11 = '1'
linha_12 = '2'
linha_13 = '3'
linha_21 = '4'
linha_22 = '5'
linha_23 = '6'
linha_31 = '7'
linha_32 = '8'
linha_33 = '9'
print('''
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
'''.format(
linha_11,
linha_12,
linha_13,
linha_21,
linha_22,
linha_23,
linha_31,
linha_32,
linha_33))
print('-'*30)
while True:
    while True:
        jogada = input('Qual sua jogada? ')
        if jogada.isnumeric() == True:
            jogada = int(jogada)
            if jogada in jogadas_totais:
                if jogada in jogadas_diponiveis:
                    jogada = int(jogada)
                    break
                else:
                    print('Essa posição ja esta oculpada, tente novamente')
        else:
            print('Jogada invalida tente novamente')
    if jogada == 1:
        linha_11 = 'x'
        if 1 in jogadas_diponiveis:
            jogadas_diponiveis.remove(1)
    if jogada == 2:
        linha_12 = 'x'
        if 2 in jogadas_diponiveis:
            jogadas_diponiveis.remove(2)
    if jogada == 3:
        linha_13 = 'x'
        if 3 in jogadas_diponiveis:
            jogadas_diponiveis.remove(3)
    if jogada == 4:
        linha_21 = 'x'
        if 4 in jogadas_diponiveis:
            jogadas_diponiveis.remove(4)
    if jogada == 5:
        linha_22 = 'x'
        if 5 in jogadas_diponiveis:
            jogadas_diponiveis.remove(5)
    if jogada == 6:
        linha_23 = 'x'
        if 6 in jogadas_diponiveis:
            jogadas_diponiveis.remove(6)
    if jogada == 7:
        linha_31 = 'x'
        if 7 in jogadas_diponiveis:
            jogadas_diponiveis.remove(7)
    if jogada == 8:
        linha_32 = 'x'
        if 8 in jogadas_diponiveis:
            jogadas_diponiveis.remove(8)
    if jogada == 9:
        if 9 in jogadas_diponiveis:
            linha_33 = 'x'
            jogadas_diponiveis.remove(9)
    jogada_79 = (7, 9)
    jogada_39 = (3, 9)
    jogada_17 = (1, 7)
    jogada_13 = (1, 3)
    jogada_1379 = (1, 3, 7, 9)

    #jogo ganho
    if jogo == '0':
        if linha_11 == 'x' and linha_12 == 'x' and linha_13 == 'x':
            print('jogo ganho')
            break
        elif linha_21 == linha_22 == linha_23 == 'x':
            print('jogo ganho')
            break
        elif linha_31 == linha_32 == linha_33 == 'x':
            print('jogo ganho')
            break
        elif linha_11 == linha_21 == linha_31 == 'x':
            print('jogo ganho')
            break
        elif linha_12 == linha_22 == linha_32 == 'x':
            print('jogo ganho')
            break
        elif linha_13 == linha_23 == linha_33 == 'x':
            print('jogo ganho')
            break
        elif linha_11 == linha_22 == linha_33 == 'x':
            print('jogo ganho')
            break
        elif linha_13 == linha_22 == linha_31 == 'x':
            print('jogo ganho')
            break

    #jogo perdido

    if linha_11 == linha_12 == linha_13 == 'o':
        print('jogo perdido')
        break
    if linha_21 == linha_22 == linha_23 == 'o':
        print('jogo perdido')
        break
    if linha_31 == linha_32 == linha_33 == 'o':
        print('jogo perdido')
        break
    if linha_11 == linha_21 == linha_31 == 'o':
        print('jogo perdido')
        break
    if linha_12 == linha_22 == linha_32 == 'o':
        print('jogo perdido')
        break
    if linha_13 == linha_23 == linha_33 == 'o':
        print('jogo perdido')
        break
    if linha_11 == linha_22 == linha_33 == 'o':
        print('jogo perdido')
        break
    if linha_13 == linha_22 == linha_31 == 'o':
        print('jogo perdido')
        break

    # jogadas vencedoras
    if jogo == 0:
        if linha_11 == 'o' and linha_13 == 'o':
            if linha_12 == '2':
                linha_12 = 'o'
                jogadas_diponiveis.remove(2)
                jogo += 1
        elif linha_21 == 'o' and linha_23 == 'o':
            if linha_22 == '2':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_31 == 'o' and linha_33 == 'o':
            if linha_32 == '8':
                linha_32 = 'o'
                jogadas_diponiveis.remove(8)
                jogo += 1
        elif linha_11 == 'o' and linha_31 == 'o':
            if linha_21 == '4':
                linha_21 = 'o'
                jogadas_diponiveis.remove(4)
                jogo += 1
        elif linha_12 == 'o' and linha_32 == 'o':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_13 == 'o' and linha_33 == 'o':
            if linha_23 == '6':
                linha_23 = 'o'
                jogadas_diponiveis.remove(6)
                jogo += 1
        elif linha_11 == 'o' and linha_33 == 'o':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_13 == 'o' and linha_31 == 'o':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1

    #jogadas para não perder
    if jogo == 0:
        if linha_11 == 'x' and linha_13 == 'x':
            if linha_12 == '2':
                linha_12 = 'o'
                jogadas_diponiveis.remove(2)
                jogo += 1
        elif linha_21 == 'x' and linha_23 == 'x':
            if linha_22 == '2':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_31 == 'x' and linha_33 == 'x':
            if linha_32 == '8':
                linha_32 = 'o'
                jogadas_diponiveis.remove(8)
                jogo += 1
        elif linha_11 == 'x' and linha_31 == 'x':
            if linha_21 == '4':
                linha_21 = 'o'
                jogadas_diponiveis.remove(4)
                jogo += 1
        elif linha_12 == 'x' and linha_32 == 'x':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_13 == 'x' and linha_33 == 'x':
            if linha_23 == '6':
                linha_23 = 'o'
                jogadas_diponiveis.remove(6)
                jogo += 1
        elif linha_11 == 'x' and linha_33 == 'x':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_13 == 'x' and linha_31 == 'x':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1

    # jogadas
    if jogo == 0:
        if jogada == 1:
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1
        elif jogada == 2:
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                jogo += 1
            elif linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1

        elif jogada == 3:
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                jogo += 1
            elif linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1
            elif linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1

        elif jogada == 4:
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1
            elif linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1

        elif jogada == 5:
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1
            elif linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1
            elif linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                jogo += 1
            elif linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1

        elif jogada == 6:
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1
            elif linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1

        elif jogada == 7:
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1
            elif linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1
            elif linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1

        elif jogada == 8:
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1
            elif linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1

        elif jogada == 9:
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1
            elif linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1
            elif linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                jogo += 1

        # jogo ganho
        if jogo == '0':
            if linha_11 == 'x' and linha_12 == 'x' and linha_13 == 'x':
                print('jogo ganho')
                break
            elif linha_21 == linha_22 == linha_23 == 'x':
                print('jogo ganho')
                break
            elif linha_31 == linha_32 == linha_33 == 'x':
                print('jogo ganho')
                break
            elif linha_11 == linha_21 == linha_31 == 'x':
                print('jogo ganho')
                break
            elif linha_12 == linha_22 == linha_32 == 'x':
                print('jogo ganho')
                break
            elif linha_13 == linha_23 == linha_33 == 'x':
                print('jogo ganho')
                break
            elif linha_11 == linha_22 == linha_33 == 'x':
                print('jogo ganho')
                break
            elif linha_13 == linha_22 == linha_31 == 'x':
                print('jogo ganho')
                break

        # jogo perdido
        if linha_11 == linha_12 == linha_13 == 'o':
            print('jogo perdido')
            break
        if linha_21 == linha_22 == linha_23 == 'o':
            print('jogo perdido')
            break
        if linha_31 == linha_32 == linha_33 == 'o':
            print('jogo perdido')
            break
        if linha_11 == linha_21 == linha_31 == 'o':
            print('jogo perdido')
            break
        if linha_12 == linha_22 == linha_32 == 'o':
            print('jogo perdido')
            break
        if linha_13 == linha_23 == linha_33 == 'o':
            print('jogo perdido')
            break
        if linha_11 == linha_22 == linha_33 == 'o':
            print('jogo perdido')
            break
        if linha_13 == linha_22 == linha_31 == 'o':
            print('jogo perdido')
            break

    jogo -= 1
    print('-' * 30)
    print('''
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
               '''.format(
        linha_11,
        linha_12,
        linha_13,
        linha_21,
        linha_22,
        linha_23,
        linha_31,
        linha_32,
        linha_33))
    print('-' * 30)
print('-' * 30)
print('''
{}  |  {}  |  {}
-----------------
{}  |  {}  |  {}
-----------------
{}  |  {}  |  {}
           '''.format(
    linha_11,
    linha_12,
    linha_13,
    linha_21,
    linha_22,
    linha_23,
    linha_31,
    linha_32,
    linha_33))
print('-' * 30)