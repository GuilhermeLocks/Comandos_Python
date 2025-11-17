from random import randint

while True:
    jogada_jogador = input('''Pedra[0], Papel[1], Tesoura[2]
Escolha:''')
    if jogada_jogador == '0' or jogada_jogador == '1' or jogada_jogador == '2':
        break
    else:
        print('Escolha invalida tente novamente.')

jogadas = ['pedra', 'papel', 'tesoura']
jogada_computador = jogadas[randint(0, len(jogadas)-1)]
print(f'Computador escolheu: {jogada_computador}')
print(f'Jogador escolheu: {jogadas[int(jogada_jogador)]}')

if jogadas[int(jogada_jogador)] == jogada_computador:
    print('Empate!')

elif jogadas[int(jogada_jogador)] == 'papel' and jogada_computador == 'tesoura':
    print('Computador ganhou!')
elif jogadas[int(jogada_jogador)] == 'pedra' and jogada_computador == 'papel':
    print('Computador ganhou!')
elif jogadas[int(jogada_jogador)] == 'tesoura' and jogada_computador == 'pedra':
    print('Computador ganhou!')

elif jogadas[int(jogada_jogador)] == 'papel' and jogada_computador == 'pedra':
    print('Jogador ganhou!')
elif jogadas[int(jogada_jogador)] == 'pedra' and jogada_computador == 'tesoura':
    print('Jogador ganhou!')
elif jogadas[int(jogada_jogador)] == 'tesoura' and jogada_computador == 'papel':
    print('Jogador ganhou!')

