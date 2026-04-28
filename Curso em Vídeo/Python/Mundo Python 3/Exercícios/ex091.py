import random
ordem = {
'primeiro': 0,
'nome_primeiro': 0,
'segundo':0,
'nome_segundo':0,
'terceiro':0,
'nome_terceiro':0,
'quarto':0,
'nome_quarto':0,
}
dicionario = {}
print('Valores sorteados:')
dicionario['jogador1']= random.randint(1, 6)
dicionario['jogador2']= random.randint(1, 6)
dicionario['jogador3']= random.randint(1, 6)
dicionario['jogador4']= random.randint(1, 6)
for c in dicionario:
    print('{} tirou {} no dado.'.format(c, dicionario[c]))
print('-='*40)
print('  == RANKING DOS JOGADORES ==')

for c in dicionario:
    if ordem['primeiro'] == 0:
        ordem['primeiro'] = dicionario[c]
        ordem['nome_primeiro'] = c
    if ordem['primeiro'] < dicionario[c]:
        ordem['primeiro'] = dicionario[c]
        ordem['nome_primeiro'] = c

for c in dicionario:
    if ordem['segundo'] == 0 and c != ordem['nome_primeiro']:
        ordem['segundo'] = dicionario[c]
        ordem['nome_segundo'] = c
    if ordem['segundo'] < dicionario[c] and c != ordem['nome_primeiro']:
        ordem['segundo'] = dicionario[c]
        ordem['nome_segundo'] = c

for c in dicionario:
    if ordem['terceiro'] == 0 and c != ordem['nome_primeiro'] and c != ordem['nome_segundo']:
        ordem['terceiro'] = dicionario[c]
        ordem['nome_terceiro'] = c
    if ordem['terceiro'] < dicionario[c] and c != ordem['nome_primeiro'] and c != ordem['nome_segundo']:
        ordem['terceiro'] = dicionario[c]
        ordem['nome_terceiro'] = c

for c in dicionario:
    if ordem['quarto'] == 0 and c != ordem['nome_primeiro'] and c != ordem['nome_segundo'] and c != ordem['nome_terceiro']:
        ordem['quarto'] = dicionario[c]
        ordem['nome_quarto'] = c
    if ordem['quarto'] < dicionario[c] and c != ordem['nome_primeiro'] and c != ordem['nome_segundo'] and c != ordem['nome_terceiro']:
        ordem['quarto'] = dicionario[c]
        ordem['nome_quarto'] = c

print('   1 lugar: {} com {}'.format(ordem['nome_primeiro'], ordem['primeiro']))
print('   2 lugar: {} com {}'.format(ordem['nome_segundo'], ordem['segundo']))
print('   3 lugar: {} com {}'.format(ordem['nome_terceiro'], ordem['terceiro']))
print('   4 lugar: {} com {}'.format(ordem['nome_quarto'], ordem['quarto']))


