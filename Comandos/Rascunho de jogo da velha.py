nome = input('Digite seu nome:')
print('Prazer,',nome,'!')

elif jogada == 2:
aleatorio_2 = random.randint(0, 1)
if jogada_79[aleatorio_2] in jogadas_diponiveis:
    jogadas_diponiveis.remove(jogada_79[aleatorio_2])
    if jogada_79[aleatorio_2] == 7 and jogada_79[aleatorio_2] != 'x':
        linha_31 = 'o'
        jogadas_diponiveis.remove(7)
    else:
        linha_33 = 'o'
        jogadas_diponiveis.remove(9)
    if jogada_79[aleatorio_2] == 9 and jogada_79[aleatorio_2] != 'x':
        linha_33 = 'o'
        jogadas_diponiveis.remove(9)
    else:
        linha_31 = 'o'
        jogadas_diponiveis.remove(7)

elif jogada == 3:
    if 7 in jogadas_diponiveis:
        linha_31 = 'o'
        jogadas_diponiveis.remove(7)

    elif jogada == 4:
    aleatorio_2 = random.randint(0, 1)
if jogada_39[aleatorio_2] in jogadas_diponiveis:
    jogadas_diponiveis.remove(jogada_39[aleatorio_2])
    if jogada_39[aleatorio_2] == 3:
        linha_13 = 'o'
    if jogada_79[aleatorio_2] == 9:
        linha_33 = 'o'

elif jogada == 5:
    aleatorio_4 = random.randint(0, 3)
if jogada_1379[aleatorio_4] in jogadas_diponiveis:
    if jogada_1379[aleatorio_4] == 1:
        if jogada_1379[aleatorio_4] in jogadas_diponiveis:
            linha_11 = 'o'
    if jogada_1379[aleatorio_4] == 3:
        if jogada_1379[aleatorio_4] in jogadas_diponiveis:
            linha_13 = 'o'
    if jogada_1379[aleatorio_4] == 7:
        if jogada_1379[aleatorio_4] in jogadas_diponiveis:
            linha_31 = 'o'
    if jogada_1379[aleatorio_4] == 9:
        if jogada_1379[aleatorio_4] in jogadas_diponiveis:
            linha_33 = 'o'
    jogadas_diponiveis.remove(jogada_1379[aleatorio_4])

elif jogada == 6:
    aleatorio_2 = random.randint(0, 1)
if jogada_17[aleatorio_2] in jogadas_diponiveis:
    jogadas_diponiveis.remove(jogada_17[aleatorio_2])
    if jogada_17[aleatorio_2] == 1:
        linha_11 = 'o'
    if jogada_17[aleatorio_2] == 7:
        linha_31 = 'o'

elif jogada == 7:
    if 3 in jogadas_diponiveis:
        linha_13 = 'o'
        jogadas_diponiveis.remove(3)

    elif jogada == 8:
    aleatorio_2 = random.randint(0, 1)
if jogada_13[aleatorio_2] in jogadas_diponiveis:
    if jogada_13[aleatorio_2] == 1:
        linha_11 = 'o'
    if jogada_13[aleatorio_2] == 3:
        linha_13 = 'o'
    jogadas_diponiveis.remove(jogada_13[aleatorio_2])

elif jogada == 9:
    if 1 in jogadas_diponiveis:
        linha_11 = 'o'
        jogadas_diponiveis.remove(1)
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
import random
aleatorio_4 = random.randint(0, 3)
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