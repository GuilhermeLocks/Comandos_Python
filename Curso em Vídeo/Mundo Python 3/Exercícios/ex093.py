dicionario = {}
lista = []
total = 0
dicionario['nome'] = str(input('Nome do jogador: '))
partida = int(input('Quantas partidas {} jogou? '.format(dicionario['nome'])))
for c in range(0, partida):
    dicionario['partida'] = partida
    gol = int(input('quantos gols na partica {}?'.format(c)))
    lista.append(gol)
    total += gol
dicionario['gol'] = lista
dicionario['total'] = total
print('-='*40)
print(dicionario)
print('-='*40)
for c in dicionario:
    print('O campo {} tem o valor {}'.format(c, dicionario[c]))
print('-='*40)
print('O jogador {} jogou {} partidas'.format(dicionario['nome'], dicionario['partida']))
for c in range(0, partida):
    print('Na partida {}, fez {} gols'.format(c, dicionario['gol'][c]))
print('foi um total de {} goals'.format(dicionario['total']))
