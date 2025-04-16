import random
pontos_1 = int(0)
pontos_2 = int(0)
while True:
    print('''Suas opções:
    
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
[ 4 ] SAIR
''')

    jogador_1 = input('Qual é a sua jogada: ')

    if jogador_1 == str(4):
        print('Fim de jogo')
        if pontos_1 > pontos_2:
            perdedor = jogador_2
            print('Placar total de {} a {} vitoria do jogador'.format(pontos_1, pontos_2))
            break
        elif pontos_2 > pontos_1:
            perdedor = jogador_1
            print('Placar total de {} a {} vitoria do computador'.format(pontos_2, pontos_1))
            break
        else:
            ganhador = 'empate'
            print('Placar total de {} a {} deu empate'.format(pontos_1, pontos_2,))
            break

    jogador_2 = random.randint(1, 3)

    if jogador_1 == str(1) or jogador_1 == str(2) or jogador_1 == str(3) or jogador_1 == str(4):
        jogador_1 = int(jogador_1)
        if jogador_1 == jogador_2:
            if jogador_1 == 1:
                print('''
jogador jogou pedra
computador jogou pedra
''')
            if jogador_1 == 2:
                print('''
jogador jogou papel
computador jogou papel
''')
            if jogador_1 == 3:
                print('''
jogador jogou tesoura
computador jogou tesoura
''')
            print('Empate')
        elif jogador_1 == 1 and jogador_2 == 2:
            print('''
jogador jogou pedra
computador jogou papel
computador ganhou
''')
            pontos_2 += 1
        elif jogador_1 == 1 and jogador_2 == 3:
            print('''
jogador jogou pedra
computador jogou tesoura
jogador ganhou
''')
            pontos_1 += 1
        elif jogador_1 == 2 and jogador_2 == 1:
            print('''
jogador jogou papel
computador jogou pedra
jogador ganhou
''')
            pontos_1 += 1
        elif jogador_1 == 2 and jogador_2 == 3:
            print('''
jogador jogou papel
computador jogou tesoura
computador ganhou
''')
            pontos_2 += 1
        elif jogador_1 == 3 and jogador_2 == 2:
            print('''
jogador jogou tesoura
computador jogou papel
jogador ganhou
''')
            pontos_1 += 1
        elif jogador_1 == 3 and jogador_2 == 1:
            print('''
jogador jogou tesoura
computador jogou pedra
computador ganhou
''')
            pontos_2 += 1
    else:
        print('''
Tente novamente.
        ''')