from random import randint

while True:
    jogada_jogador = input('''Pedra[0], Papel[1], Tesoura[2]
Escolha:''')
    if jogada_jogador == '0' or jogada_jogador == '1' or jogada_jogador == '2':
        break
    else:
        print('Escolha invalida tente novamente.')

jogadas = ['pedra', 'papel', 'tesoura']
print(f'Computador escolheu: {jogadas[randint(0, len(jogadas)-1)]}')
print(f'Jogador escolheu: {jogadas[int(jogada_jogador)]}')

if jogadas[int(jogada_jogador)] == jogadas[randint(0, len(jogadas)-1)]:
    print('Empate!')

