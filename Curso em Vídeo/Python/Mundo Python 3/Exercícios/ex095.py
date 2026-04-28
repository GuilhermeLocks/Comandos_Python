dicionario = {}
lista = []
jogadores  = []
total = 0
continuar = ''

while continuar != 'N':

    dicionario['nome'] = str(input('Nome do jogador: '))
    partida = int(input('Quantas partidas {} jogou? '.format(dicionario['nome'])))

    for c in range(0, partida):
        dicionario['partida'] = partida
        gol = int(input('quantos gols na partica {}?'.format(c)))
        lista.append(gol)
        total += gol
    dicionario['gol'] = lista
    dicionario['total'] = total

    jogadores.append(dicionario.copy())
    dicionario.clear()
    lista = []
    total = 0

    while True:
        continuar = input('Quer continuar? [N/S]').upper()
        if continuar == 'N' or continuar == 'S':
            break
        else:
            print('ERRO! Por fazer, digitar apenas com S ou N.')

print('-='*40)
print('cod nome          gols          total')
print('-'*30)
for c in range(0, len(jogadores)):
    print('  {} {} {} {}'.format(c, jogadores[c]['nome'], jogadores[c]['gol'], jogadores[c]['total']))
print('-'*30)
jogador = -1
while jogador != 999:

    while True:
        jogador = input('Mostrar dados de qual jogador? (999 para parar)')
        if jogador.isnumeric() == True:
            jogador = int(jogador)
            if jogador == 999:
                break
            for c in range(0, len(jogadores)):
                if jogador == c:
                    print('-'*30)
                    print('cod nome          gols          total')
                    print('  {} {}        {}        {}'.format(jogador, jogadores[jogador]['nome'], jogadores[jogador]['gol'], jogadores[jogador]['total']))
                    print('-' * 30)
        else:
            print('ERRO! jogador invalido, tente novamente.')



