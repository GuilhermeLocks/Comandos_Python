dados = {}
dicionario = dict()
dados = {'nome':'pedro', 'idade':'25'}
dados['sexo'] = 'M'
print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])
del dados['idade']
print('')
print(dados)
dados['idade'] = 6
print('')
print(dados.values())
print(dados.keys())
print(dados.items())
print('')
for k, v in dados.items():
    print('O {} é {},'.format(k, v), end=' ')
print('.')
for c in dados:
    print('O {} é {}.'.format(c, dados[c]), end=' ')
print('')