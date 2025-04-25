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