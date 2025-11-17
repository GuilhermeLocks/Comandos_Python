times = ('Flamengo', 'Palmeiras', 'Bragantino', 'Cruzeiro', 'Fluminense', 'Internacional', 'Bahia', 'Botafogo', 'Ceará', 'São Paulo', 'Vasco', 'Corinthians', 'Juventude', 'Mirassol', 'Fortaleza', 'Vitória', 'Atlético-MG', 'Grêmio', 'Santos', 'Sport')
print('Os 5 primeiros colocados são {}'.format(times[0:5]))
print('Os 4 ultimos colocados são {}'.format(times[-4:]))
print('A lista em ordem alfabetica é')
print(sorted(times))
for posicao, c in enumerate(times):
    if c == 'Palmeiras':
        print('A posição do Palmeiras e {}° lugar'.format(posicao+1))