def campeonato(nome, gol=0):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = 0
    print('O jogador {} fez {} gol(s) no campeonato'. format(nome, gol))

print('-'*30)
campeonato(input('Nome do jogador: '), input('Número de Gols: '))