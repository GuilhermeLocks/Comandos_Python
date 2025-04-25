import random

jogadas_totais = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogadas_diponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogo = 0
linha_11 = '1'
linha_12 = '2'
linha_13 = '3'
linha_21 = '4'
linha_22 = '5'
linha_23 = '6'
linha_31 = '7'
linha_32 = '8'
linha_33 = '9'
jogada_79 = (7, 9)
jogada_39 = (3, 9)
jogada_17 = (1, 7)
jogada_13 = (1, 3)
jogada_1379 = (1, 3, 7, 9)

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

    # jogada do jogador

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

    # jogadas

    if jogada == 1:
        if 1 in jogadas_diponiveis:
            linha_11 = 'x'
            jogadas_diponiveis.remove(1)

    if jogada == 2:
        if 2 in jogadas_diponiveis:
            linha_12 = 'x'
            jogadas_diponiveis.remove(2)

    if jogada == 3:
        if 3 in jogadas_diponiveis:
            linha_13 = 'x'
            jogadas_diponiveis.remove(3)

    if jogada == 4:
        if 4 in jogadas_diponiveis:
            linha_21 = 'x'
            jogadas_diponiveis.remove(4)

    if jogada == 5:
        if 5 in jogadas_diponiveis:
            linha_22 = 'x'
            jogadas_diponiveis.remove(5)

    if jogada == 6:
        if 6 in jogadas_diponiveis:
            linha_23 = 'x'
            jogadas_diponiveis.remove(6)

    if jogada == 7:
        if 7 in jogadas_diponiveis:
            linha_31 = 'x'
            jogadas_diponiveis.remove(7)

    if jogada == 8:
        if 8 in jogadas_diponiveis:
            linha_32 = 'x'
            jogadas_diponiveis.remove(8)

    if jogada == 9:
        if 9 in jogadas_diponiveis:
            linha_33 = 'x'
            jogadas_diponiveis.remove(9)

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

    if linha_11 == 'o' and linha_13 == 'o':
        if linha_12 == '2':
            linha_12 = 'o'
            jogadas_diponiveis.remove(2)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_11 == 'o' and linha_12 == 'o':
        if linha_13 == '3':
            linha_12 = 'o'
            jogadas_diponiveis.remove(3)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_12 == 'o' and linha_13 == 'o':
        if linha_11 == '1':
            linha_11 = 'o'
            jogadas_diponiveis.remove(1)
            print('-' * 30)
            print('jogo perdido')
            break

    elif linha_21 == 'o' and linha_23 == 'o':
        if linha_22 == '2':
            linha_22 = 'o'
            jogadas_diponiveis.remove(5)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_21 == 'o' and linha_22 == 'o':
        if linha_23 == '6':
            linha_23 = 'o'
            jogadas_diponiveis.remove(6)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_22 == 'o' and linha_23 == 'o':
        if linha_21 == '4':
            linha_22 = 'o'
            jogadas_diponiveis.remove(4)
            print('-' * 30)
            print('jogo perdido')
            break

    elif linha_31 == 'o' and linha_33 == 'o':
        if linha_32 == '8':
            linha_32 = 'o'
            jogadas_diponiveis.remove(8)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_31 == 'o' and linha_32 == 'o':
        if linha_33 == '9':
            linha_33 = 'o'
            jogadas_diponiveis.remove(9)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_32 == 'o' and linha_33 == 'o':
        if linha_31 == '7':
            linha_31 = 'o'
            jogadas_diponiveis.remove(7)
            print('-' * 30)
            print('jogo perdido')
            break

    elif linha_11 == 'o' and linha_31 == 'o':
        if linha_21 == '4':
            linha_21 = 'o'
            jogadas_diponiveis.remove(4)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_11 == 'o' and linha_21 == 'o':
        if linha_31 == '7':
            linha_31 = 'o'
            jogadas_diponiveis.remove(7)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_21 == 'o' and linha_31 == 'o':
        if linha_11 == '1':
            linha_11 = 'o'
            jogadas_diponiveis.remove(1)
            print('-' * 30)
            print('jogo perdido')
            break

    elif linha_12 == 'o' and linha_32 == 'o':
        if linha_22 == '5':
            linha_22 = 'o'
            jogadas_diponiveis.remove(5)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_12 == 'o' and linha_22 == 'o':
        if linha_32 == '8':
            linha_32 = 'o'
            jogadas_diponiveis.remove(8)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_22 == 'o' and linha_32 == 'o':
        if linha_12 == '2':
            linha_12 = 'o'
            jogadas_diponiveis.remove(2)
            print('-' * 30)
            print('jogo perdido')
            break

    elif linha_13 == 'o' and linha_33 == 'o':
        if linha_23 == '6':
            linha_23 = 'o'
            jogadas_diponiveis.remove(6)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_13 == 'o' and linha_23 == 'o':
        if linha_33 == '9':
            linha_33 = 'o'
            jogadas_diponiveis.remove(9)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_23 == 'o' and linha_33 == 'o':
        if linha_13 == '3':
            linha_13 = 'o'
            jogadas_diponiveis.remove(3)
            print('-' * 30)
            print('jogo perdido')
            break

    elif linha_11 == 'o' and linha_33 == 'o':
        if linha_22 == '5':
            linha_22 = 'o'
            jogadas_diponiveis.remove(5)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_11 == 'o' and linha_22 == 'o':
        if linha_33 == '9':
            linha_33 = 'o'
            jogadas_diponiveis.remove(9)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_22 == 'o' and linha_33 == 'o':
        if linha_11 == '1':
            linha_11 = 'o'
            jogadas_diponiveis.remove(1)
            print('-' * 30)
            print('jogo perdido')
            break

    elif linha_13 == 'o' and linha_31 == 'o':
        if linha_22 == '5':
            linha_22 = 'o'
            jogadas_diponiveis.remove(5)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_13 == 'o' and linha_22 == 'o':
        if linha_31 == '7':
            linha_31 = 'o'
            jogadas_diponiveis.remove(7)
            print('-' * 30)
            print('jogo perdido')
            break
    elif linha_22 == 'o' and linha_31 == 'o':
        if linha_13 == '3':
            linha_13 = 'o'
            jogadas_diponiveis.remove(3)
            print('-' * 30)
            print('jogo perdido')
            break

    #jogadas para não o computador não perder

    if jogo == 0:

        if linha_11 == 'x' and linha_13 == 'x':
            if linha_12 == '2':
                linha_12 = 'o'
                jogadas_diponiveis.remove(2)
                jogo += 1
        elif linha_11 == 'x' and linha_12 == 'x':
            if linha_13 == '3':
                linha_12 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1
        elif linha_12 == 'x' and linha_13 == 'x':
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1

        elif linha_21 == 'x' and linha_23 == 'x':
            if linha_22 == '2':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_21 == 'x' and linha_22 == 'x':
            if linha_23 == '6':
                linha_22 = 'o'
                jogadas_diponiveis.remove(6)
                jogo += 1
        elif linha_22 == 'x' and linha_23 == 'x':
            if linha_21 == '4':
                linha_22 = 'o'
                jogadas_diponiveis.remove(4)
                jogo += 1

        elif linha_31 == 'x' and linha_33 == 'x':
            if linha_32 == '8':
                linha_32 = 'o'
                jogadas_diponiveis.remove(8)
                jogo += 1
        elif linha_31 == 'x' and linha_32 == 'x':
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1
        elif linha_32 == 'x' and linha_33 == 'x':
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                jogo += 1

        elif linha_11 == 'x' and linha_31 == 'x':
            if linha_21 == '4':
                linha_21 = 'o'
                jogadas_diponiveis.remove(4)
                jogo += 1
        elif linha_11 == 'x' and linha_21 == 'x':
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                jogo += 1
        elif linha_21 == 'x' and linha_31 == 'x':
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1

        elif linha_12 == 'x' and linha_32 == 'x':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_12 == 'x' and linha_22 == 'x':
            if linha_32 == '8':
                linha_32 = 'o'
                jogadas_diponiveis.remove(8)
                jogo += 1
        elif linha_22 == 'x' and linha_32 == 'x':
            if linha_12 == '2':
                linha_12 = 'o'
                jogadas_diponiveis.remove(2)
                jogo += 1

        elif linha_13 == 'x' and linha_33 == 'x':
            if linha_23 == '6':
                linha_23 = 'o'
                jogadas_diponiveis.remove(6)
                jogo += 1
        elif linha_13 == 'x' and linha_23 == 'x':
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1
        elif linha_23 == 'x' and linha_33 == 'x':
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1

        elif linha_11 == 'x' and linha_33 == 'x':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_11 == 'x' and linha_22 == 'x':
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1
        elif linha_22 == 'x' and linha_33 == 'x':
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1

        elif linha_13 == 'x' and linha_31 == 'x':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_13 == 'x' and linha_22 == 'x':
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                jogo += 1
        elif linha_22 == 'x' and linha_31 == 'x':
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1

    # jogadas
    print(jogo)
    if jogo == 0:
        if jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis))-1)] == 0 and linha_11 == '1':
            linha_11 = 'o'
            jogadas_diponiveis.remove(1)
            jogo += 1
    if jogo == 0:
        if jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis))-1)] == 1 and linha_12 == '2':
            linha_12 = 'o'
            jogadas_diponiveis.remove(2)
            jogo += 1
    if jogo == 0:
        if jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis))-1)] == 2 and linha_13 == '3':
            linha_13 = 'o'
            jogadas_diponiveis.remove(3)
            jogo += 1
    if jogo == 0:
        if jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis))-1)] == 3 and linha_21 == '4':
            linha_21 = 'o'
            jogadas_diponiveis.remove(4)
            jogo += 1
    if jogo == 0:
        if jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis))-1)] == 4 and linha_22 == '5':
            linha_22 = 'o'
            jogadas_diponiveis.remove(5)
            jogo += 1
    if jogo == 0:
        if jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis))-1)] == 5 and linha_23 == '6':
            linha_23 = 'o'
            jogadas_diponiveis.remove(6)
            jogo += 1
    if jogo == 0:
        if jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis))-1)] == 6 and linha_31 == '7':
            linha_31 = 'o'
            jogadas_diponiveis.remove(7)
            jogo += 1
    if jogo == 0:
        if jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis))-1)] == 7 and linha_32 == '8':
            linha_32 = 'o'
            jogadas_diponiveis.remove(8)
            jogo += 1
    if jogo == 0:
        if jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis))-1)] == 8 and linha_33 == '9':
            linha_33 = 'o'
            jogadas_diponiveis.remove(9)
            jogo += 1

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