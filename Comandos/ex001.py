import random
aleatorio_4 = random.randint(0, 3)
jogadas_totais = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogadas_diponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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
    jogada = input('Qual sua jogada? ')
    if jogada.isnumeric() == True:
        jogada = int(jogada)
        if jogada in jogadas_totais:
            if jogada in jogadas_diponiveis:
                jogada = int(jogada)
            else:
                print('Essa posição ja esta oculpada, tente novamente.1')
    else:
        print('Jogada invalida tente novamente.2')
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
        linha_33 = 'x'
        if 9 in jogadas_diponiveis:
            jogadas_diponiveis.remove(9)
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
    jogada_79 = (7, 9)
    jogada_39 = (3, 9)
    jogada_17 = (1, 7)


    if jogada == 1:
        linha_33 = 'o'
        if 9 in jogadas_diponiveis:
            jogadas_diponiveis.remove(9)

    if jogada == 2:
        aleatorio_2 = random.randint(0, 1)
        if jogada_79[aleatorio_2] in jogadas_diponiveis:
            jogadas_diponiveis.remove(jogada_79[aleatorio_2])
            print(jogada_79[aleatorio_2])
            if jogada_79[aleatorio_2] == 7:
                linha_31 = 'o'
            if jogada_79[aleatorio_2] == 9:
                linha_33 = 'o'

    if jogada == 3:
        linha_31 = 'o'
        if 7 in jogadas_diponiveis:
            jogadas_diponiveis.remove(7)

    if jogada == 4:
        aleatorio_2 = random.randint(0, 1)
        if jogada_39[aleatorio_2] in jogadas_diponiveis:
            jogadas_diponiveis.remove(jogada_39[aleatorio_2])
            print(jogada_39[aleatorio_2])
            if jogada_39[aleatorio_2] == 3:
                linha_13 = 'o'
            if jogada_79[aleatorio_2] == 9:
                linha_33 = 'o'

    #if jogada == 5:
        #1, 3, 7, 9

    if jogada == 6:
        aleatorio_2 = random.randint(0, 1)
        if jogada_17[aleatorio_2] in jogadas_diponiveis:
            jogadas_diponiveis.remove(jogada_17[aleatorio_2])
            if jogada_17[aleatorio_2] == 1:
                linha_11 = 'o'
            if jogada_17[aleatorio_2] == 7:
                linha_31 = 'o'

    if jogada == 7:
        linha_13 = 'o'
        if 3 in jogadas_diponiveis:
            jogadas_diponiveis.remove(3)

    #if jogada == 8:
        # 1, 3

    if jogada == 9:
        linha_11 = 'o'
        if 1 in jogadas_diponiveis:
            jogadas_diponiveis.remove(1)

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